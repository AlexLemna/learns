Function Create-SemesterGrades
{
    # Grades from Mainframe
    #
    $GradeArray = @("Will Smith","FA","CIS1160","Introduction to Powershell",3,"B",3)
    $GradeArray += @("Will Smith","FA","CIS1610","Windows Client O/S",4,"B",4)
    $GradeArray += @("Will Smith","FA","CIS1120","Introduction to Networking",3,"B",4)
    $GradeArray

} # End Create-SemesterGrades

Function Print-ReportCard
{
$GradeArray = @([PSCustomObject]@{
    Name = "Will Smith                                 "
    Semester= "FA"
    Course= "CIS1160"
    CourseName = "Introduction to PowerShell"
    Hours =3
    LetterGrade = "B"
    PointGrade = 3
    },

[PSCustomObject]@{
    Name = "Will Smith                                 "
    Semester= "FA"
    Course= "CIS1610"
    CourseName = "Windows Client O/S        "
    Hours =4
    LetterGrade = "A"
    PointGrade = 4
    },

[PSCustomObject]@{
    Name = "Will Smith                                 "
    Semester= "FA"
    Course= "CIS1120"
    CourseName = "Introduction to Networking"
    Hours =3
    LetterGrade = "A"
    PointGrade = 4
    })


# Get the report card header information and print it to the screen

    $Work = $GradeArray[0].Name + "    "
    $Student = $work.substring(0,20)

    $Semester = $GradeArray[0].Semester

    Write-Host "_______________________________________________________"
    Write-Host "$Student                       Semester: $Semester"
    Write-Host "_______________________________________________________"
    Write-Host ""
    Write-Host "_______________________________________________________"
    Write-Host "Course       Course Name       Hours Grade Grade Points"
    Write-Host "_______________________________________________________"

# Now loop through all the detail, printing one line for each detail item. Remember to
# calculate the total grade points for computing the average later.

    $TotalHours = 0
    $TotalPoints = 0

    for ($i = 0 ; $i -lt 3 ; $i = $i + 1)
    {
        
        $TotalHours = $TotalHours + $GradeArray[$i].Hours

        $GradePoints = $GradeArray[$i].Hours * $GradeArray[$i].PointGrade
        $TotalPoints = $TotalPoints + $GradePoints

        $Work = $GradeArray[$i].CourseName + " "
        $CourseDescription = $Work.substring(0,26)

        Write-Host $GradeArray[$i].Course, " ", $CourseDescription, " ", $GradeArray[$i].Hours, "", $GradeArray[$i].LetterGrade, "    ", $GradeArray[$i].PointGrade, "   ", $GradePoints

    }

    # All done, now calculate the average and print to screen.
    
    Write-Host ""
    Write-Host "_______________________________________________________"
    $Average = $TotalPoints / $TotalHours
    Write-Host "Average: $Average"

} # End Print-ReportCard