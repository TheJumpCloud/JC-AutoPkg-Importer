Param(
    [Parameter(Mandatory = $true, ValueFromPipelineByPropertyName = $true, Position = 0)][ValidateNotNullOrEmpty()][System.String]$JumpCloudApiKey
)
Try
{
    Install-Module -Repository:('PSGallery') -Name:('JumpCloud') -Force
    # Authenticate to JumpCloud
    Connect-JCOnline -JumpCloudApiKey:($JumpCloudApiKey) -force | Out-Null

    # Clean up AutoPkg Commands and System Groups

    # Specifically the Firefox Groups:
    $firefoxGroups = Get-JCGroup -type System | Where-Object name -Like AutoPkg-Firefox* | Select-Object name
    foreach ($i in $firefoxGroups) {
        Remove-JCSystemGroup  $i -force
    }
    # Specifically Firefox Commands
    $firefoxCommand = Get-JCCommand | Where-Object name -Like AutoPkg-Firefox* | select-object id
    foreach ($i in $firefoxCommand) {
        Remove-JCCommand -CommandID $i -force
    }
}
Catch
{
    Write-Error ($_)
}
