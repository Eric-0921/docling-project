# :SYSTem:ERRor:HISTory?
Queries the error history.

Note that the result can amount several kilobytes.


## Return values:
<ErrorHistory>

string

Operating Manual 1407.0806.32 ─ 23

440

R&S ® SMB100A

Example:                SYSTEM: ERROR: HISTORY?


SYSTEM:ERR:HISTORY?
                  // 90,"Info:(*)Instrument startup... (Mar-13-2017/ 10:25:16-601 ms)",
                  90,"Info:(*)Information generated while processing license keys...",
                  Repaired Error!
                  COND: ( hr == false )
                  FILE: /home/sa_okbuildserver/jenkins/workspace/OK-Legacy-Distribution-30/
                  ok_services_oklib/Src/CServiceExtension.cpp
                  LINE: 3554
                  ADDITIONAL INFO: Init ServiceExtension failed, 2877, -2147211613
                  HRESULT = 800010007
                  ", 90,"[RF A] No frequency calibration data found.
                  Please run Adjust All!", ...
                  // returns all entries of the error queue

                  Query only

Usage:

Query only

Manual operation:

See "History" on page 74

