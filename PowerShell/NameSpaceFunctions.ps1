Function Get-WMINameSpace
{
    Param(
        $namespace = "root",
        $computer = "localhost"
        )
    Get-WMIObject -class __NAMESPACE  -computer $computer -namespace $namespace -ErrorAction "SilentlyContinue" |
        Foreach-Object `
        -Process `
        {
            $subNS = Join-Path  -Path  $_.__NAMESPACE  -ChildPath $_.name
            If($subNS  -notmatch 'directory') {$subNS}
            $namespaces += $subNS + "'r'n"
            Get-WMINameSpace  -namespace $subNS  -computer $computer
        }
} 
