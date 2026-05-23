param(
    [switch]$Force,
    [string]$CodexHome = $env:CODEX_HOME
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($CodexHome)) {
    $CodexHome = Join-Path $HOME ".codex"
}

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$Source = Join-Path $RepoRoot "skills\pdf-to-docx-humanize"
$SkillsRoot = Join-Path $CodexHome "skills"
$Destination = Join-Path $SkillsRoot "pdf-to-docx-humanize"

if (-not (Test-Path $Source)) {
    throw "Skill source not found: $Source"
}

New-Item -ItemType Directory -Path $SkillsRoot -Force | Out-Null

if (Test-Path $Destination) {
    if (-not $Force) {
        Write-Host "Destination already exists: $Destination"
        Write-Host "Run again with -Force to replace it."
        exit 2
    }
    Remove-Item -LiteralPath $Destination -Recurse -Force
}

Copy-Item -Path $Source -Destination $Destination -Recurse

Write-Host "Installed pdf-to-docx-humanize to:"
Write-Host "  $Destination"

$Deps = @("humanize", "humanize-gen-plan", "humanize-refine-plan", "humanize-rlcr")
$Missing = @()
foreach ($Dep in $Deps) {
    if (-not (Test-Path (Join-Path $SkillsRoot $Dep))) {
        $Missing += $Dep
    }
}

if ($Missing.Count -gt 0) {
    Write-Host ""
    Write-Host "Warning: full RLCR workflow needs these missing skills:"
    foreach ($Item in $Missing) {
        Write-Host "  - $Item"
    }
    Write-Host "Install the humanize skill family, then restart Codex."
} else {
    Write-Host ""
    Write-Host "Humanize dependency check passed."
}

Write-Host ""
Write-Host "Restart Codex, then invoke: `$pdf-to-docx-humanize"
