#include <iostream>
#include <Windows.h>
#include <TlHelp32.h>

int main()
{
	PROCESSENTRY32 pe32{};
	pe32.dwSize = sizeof(PROCESSENTRY32);

	HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
	if (snapshot == INVALID_HANDLE_VALUE) {
		
		
		return 1;
	}

	if (Process32First(snapshot, &pe32))
	{
		do
		{
			std::wcout << pe32.szExeFile << std::endl;
		} while (Process32Next(snapshot, &pe32));
	}

	CloseHandle(snapshot);
	return 0;
}