#include <iostream>
#include <windows.h>

int main()
{
/*BOOL CreateProcessW(
  [in, optional]      LPCWSTR               lpApplicationName,
  [in, out, optional] LPWSTR                lpCommandLine,
  [in, optional]      LPSECURITY_ATTRIBUTES lpProcessAttributes,
  [in, optional]      LPSECURITY_ATTRIBUTES lpThreadAttributes,
  [in]                BOOL                  bInheritHandles,
  [in]                DWORD                 dwCreationFlags,
  [in, optional]      LPVOID                lpEnvironment,
  [in, optional]      LPCWSTR               lpCurrentDirectory,
  [in]                LPSTARTUPINFOW        lpStartupInfo,
  [out]               LPPROCESS_INFORMATION lpProcessInformation
);*/
STARTUPINFOW si = { 0 };
PROCESS_INFORMATION pi = { 0 };
    if(!CreateProcessW(L"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk", NULL, NULL, NULL, FALSE, BELOW_NORMAL_PRIORITY_CLASS, NULL, NULL, &si, &pi)){
        printf("(-) Failed to Create Process, Error: %ld", GetLastError());
        return EXIT_FAILURE;
    };

    return 0;
}