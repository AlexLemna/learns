Function Create-DataFiles
{
    # Create the Students file
    Set-Content -Path C:\mytest\Students.txt -Value "Will Smith"
    Add-Content C:\mytest\Students.txt -Value "Mary Jones"
    Add-Content C:\mytest\Students.txt -Value "Ian Baker"
    Get-Content C:\mytest\Students.txt

    # Create the Grades file
    Set-Content -Path C:\mytest\Grades.txt -Value "A"
    Add-Content C:\mytest\Grades.txt -Value "B"
    Add-Content C:\mytest\Grades.txt -Value "C"
    Add-Content C:\mytest\Grades.txt -Value "D"
    Add-Content C:\mytest\Grades.txt -Value "F"
    Get-Content C:\mytest\Grades.txt
} # End Create-DataFiles