Function Get-WmiProvider
{
    Param(
        [string]$nameSpace,
        [string]$computer
        )
    Get-CimINstance -ClassName __Provider -NameSpace $namespace | Sort-Object -property Name | Select-Object name
} #end function Get-WmiProvider

Get-WmiProvider -namespace root\cimv2 -computer $env:COMPUTERNAME