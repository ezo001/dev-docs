@echo off
REM Add a new docs section under MD/ (landing page + config).
REM Usage: add_docs_section.bat [id] [label] [md-folder]
REM   id         = section ID for URL (e.g. aot -> /aot/)
REM   label      = navbar label (optional)
REM   md-folder  = MD subfolder name (optional; default = id). Use to match DOCX/AOT -> MD/AOT.
REM Example: add_docs_section.bat aot "AOT Foundation" AOT

set ID=%~1
set LABEL=%~2
set MDFOLDER=%~3

if "%ID%"=="" (
  set /p ID="Enter section ID (e.g. aot): "
  if "%ID%"=="" exit /b 1
)

cd /d "%~dp0"
if "%MDFOLDER%"=="" (
  if "%LABEL%"=="" (
    python add_docs_section.py "%ID%"
  ) else (
    python add_docs_section.py "%ID%" "%LABEL%"
  )
) else (
  if "%LABEL%"=="" (
    python add_docs_section.py "%ID%" --md-folder "%MDFOLDER%"
  ) else (
    python add_docs_section.py "%ID%" "%LABEL%" --md-folder "%MDFOLDER%"
  )
)
pause
