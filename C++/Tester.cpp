#include <iostream>
#include <windows.h>
#include <stdio.h>

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
  STARTUPINFO si = {0};
  PROCESS_INFORMATION pi = {0};

  if (!CreateProcessW(L"C:\\Users\\IT\\Downloads\\rufus-4.6.exe", NULL, NULL, FALSE, 0, NULL, NULL, si, pi)) {
    printf("(-) Failed to create process, error: %ld", GetLastError());
    return 0;
  };

  printf("(+) process started! pid: %ld", pi.dwProcessId);
  return 0;
}