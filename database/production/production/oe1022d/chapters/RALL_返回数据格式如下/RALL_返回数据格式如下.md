## RALL? 返回数据格式如下：

| 分类 | 返回数据 | 数据位置 |
|---|---|---|
| 测量数据 | 50 个 A 通道 X 值（ 64 位浮点数） | 0~399 |
|  | 50 个 A 通道 Y 值（ 64 位浮点数） | 400~799 |
|  | 50 个 A 通道频率值（ 64 位浮点数） | 800~1199 |
|  | 50 个 A 通道 Noise 值（ 64 位浮点数） | 1200~1599 |
|  | 50 个 A 通道 Xh1 值（ 64 位浮点数） | 1600~1999 |
|  | 50 个 A 通道 Yh1 值（ 64 位浮点数） | 2000~2399 |
|  | 50 个 A 通道 Xh2 值（ 64 位浮点数） | 2400~2799 |
|  | 50 个 A 通道 Yh2 值（ 64 位浮点数） | 2800~3199 |
|  | 50 个 B 通道 X 值（ 64 位浮点数） | 3200~3599 |
|  | 50 个 B 通道 Y 值（ 64 位浮点数） | 3600~3999 |
|  | 50 个 B 通道频率值（ 64 位浮点数） | 4000~4399 |
|  | 50 个 B 通道 Noise 值（ 64 位浮点数） | 4400~4799 |
|  | 50 个 B 通道 Xh1 值（ 64 位浮点数） | 4800~5199 |
|  | 50 个 B 通道 Yh1 值（ 64 位浮点数） | 5200~5599 |
|  | 50 个 B 通道 Xh2 值（ 64 位浮点数） | 5600~5999 |
|  | 50 个 B 通道 Yh2 值（ 64 位浮点数） | 6000~6399 |
|  | 50 个 AUXADC1 值（ 64 位浮点数） | 6400~6799 |
|  | 50 个 AUXADC2 值（ 64 位浮点数） | 6800~7199 |
|  | 50 个 AUXADC3 值（ 64 位浮点数） | 7200~7599 |
|  | 50 个 AUXADC4 值（ 64 位浮点数） | 7600~7999 |
| 通道 Ref Phase 配置参数 | <Ref.Phase> 设置（ 32 位浮点数） | 8200~8203 |
|  | <Ref.Source> 设置（ 8 位整型数） | 8204 |
|  | 当前频率值（ 64 位浮点数） | 8205~8212 |
|  | 内部频率值（ 64 位浮点数） | 8213~8220 |
|  | <Ref.slope> 设置（ 8 位整型数） | 8221 |
|  | <Harmonic 1> 设置（ 64 位整型数） | 8222~8229 |
|  | <Harmonic 2> 设置（ 64 位整型数） | 8230~8237 |


<!-- image -->


<!-- Page 83 -->

OE1022D DSP Lock-In Amplifier

77

| <Sweep Type> 设置（ 8 位整型数） | 8246 |
|---|---|
| <SweepStartFreq> 设置（ 64 位浮点数） | 8247~8254 |
| <SweepStopFreq> 设置（ 64 位浮点数） | 8255~8262 |
| <SweepStepFreq> 设置（ 64 位浮点数） | 8263~8270 |
| <SweepStepPerc> 设置（ 32 位浮点数） | 8271~8274 |
| <Sweep Time> 设置（ 64 位整型数） | 8275~8282 |
| <Sweep Run> 设置（ 8 位整型数） | 8283 |
| <Sineout Voltage> 设置（ 32 位浮点数） | 8292~8295 |
| <SweepMode> 设置（ 8 位整型数） | 8296 |
| <SweepSartVolt> 设置（ 32 位浮点数） | 8297~8300 |
| <SweepStopVolt> 设置（ 32 位浮点数） | 8301~8304 |
| <SweepStepVolt> 设置（ 32 位浮点数） | 8305~8308 |
| <SweepStepPrecent> 设置（ 32 位浮点数） | 8309~8312 |
| <Sweep Time> 设置（ 64 位整型数） | 8313~8320 |
| <Sineout Sweep Run> 设置（ 8 位整型数） | 8321 |
| <Sineout DC Voltage> 设置（ 32 位浮点数） | 8322~8325 |
| <Equation C1> 设置（ 64 位浮点数） | 8330~8337 |
| <Equation C2> 设置（ 64 位浮点数） | 8338~8345 |
| <Equation1 A> 源设置（ 8 位整型数） | 8346 |
| <Equation2 A> 源设置（ 8 位整型数） | 8347 |
| <Equation3 A> 源设置（ 8 位整型数） | 8348 |
| <Equation4 A> 源设置（ 8 位整型数） | 8349 |
| <Equation1 B> 源设置（ 8 位整型数） | 8350 |
| <Equation2 B> 源设置（ 8 位整型数） | 8351 |
| <Equation3 B> 源设置（ 8 位整型数） | 8352 |
| <Equation4 B> 源设置（ 8 位整型数） | 8353 |
| <Equation1 C> 源设置（ 8 位整型数） | 8354 |
| <Equation2 C> 源设置（ 8 位整型数） | 8355 |
| <Equation3 C> 源设置（ 8 位整型数） | 8356 |
| <Equation4 C> 源设置（ 8 位整型数） | 8357 |
| <Sensitivity> 设置（ 8 位整型数） | 8390 |
| <Reserve> 设置（ 8 位整型数） | 8391 |
| <Source> 设置（ 8 位整型数） | 8392 |
| <Grounding> 设置（ 8 位整型数） | 8393 |
| <Coupling> 设置（ 8 位整型数） | 8394 |
| <Line Notch> 设置（ 8 位整型数） | 8395 |
| <Time Constant> 设置（ 8 位整型数） | 8404 |
| <Filter dB/oct> 设置（ 8 位整型数） | 8405 |
| <Synchronous> 设置（ 8 位整型数） | 8406 |


<!-- image -->


<!-- Page 84 -->

78

OE1022D DSP Lock-In Amplifier

| <CH1 Output Source> 设置（ 8 位整型数） | 8415 |
|---|---|
| <CH2 Output Source> 设置（ 8 位整型数） | 8416 |
| <CH1 Offset> 设置（ 32 位浮点数） | 8417~8420 |
| <CH2 Offset> 设置（ 32 位浮点数） | 8421~8424 |
| <CH1 Expand> 设置（ 16 位整型数） | 8425~8426 |
| <CH2 Expand> 设置（ 16 位整型数） | 8427~8428 |
| <CH1 Output Speed> 设置（ 8 位整型数） | 8429 |
| <CH2 Output Speed> 设置（ 8 位整型数） | 8430 |
| <CH1 AUXOUT> 值设置（ 32 位浮点数） | 8431~8434 |
| <CH2 AUXOUT> 值设置（ 32 位浮点数） | 8435~8438 |
| <Sample Time> 设置（ 64 位浮点数） | 8441~8448 |
| <Sample Length> 设置（ 64 位整型数） | 8449~8456 |
| <Sample Buffer1> 设置（ 8 位整型数） | 8457 |
| <Sample Buffer2> 设置（ 8 位整型数） | 8458 |
| <Sample Buffer3> 设置（ 8 位整型数） | 8459 |
| <Sample Buffer4> 设置（ 8 位整型数） | 8460 |
| <Sample Trigger Mode> 设置（ 8 位整型数） | 8461 |
| <Sample Mode> 设置（ 8 位整型数） | 8462 |
| <Sample Current Point> 设置 （ 64 位整型数） | 8463~8470 |
| Input Overload 状态（ 8 位整型数） | 8479 |
| Gain Overload 状态（ 8 位整型数） | 8480 |
| PLL LOCKED 状态（ 8 位整型数） | 8481 |
| <Ref.Phase> 设置（ 32 位浮点数） | 8500~8503 |
| <Ref.Source> 设置（ 8 位整型数） | 8504 |
| 当前频率值（ 64 位浮点数） | 8505~8512 |
| 内部频率值（ 64 位浮点数） | 8513~8520 |
| <Ref.slope> 设置（ 8 位整型数） | 8521 |
| <Harmonic 1> 设置（ 64 位整型数） | 8522~8529 |
| <Harmonic 2> 设置（ 64 位整型数） | 8530~8537 |
| <Sweep Type> 设置（ 8 位整型数） | 8546 |
| <SweepStartFreq> 设置（ 64 位浮点数） | 8547~8554 |
| <SweepStopFreq> 设置（ 64 位浮点数） | 8555~8562 |
| <SweepStepFreq> 设置（ 64 位浮点数） | 8563~8570 |
| <SweepStepPercent> 设置（ 32 位浮点数） | 8571~8574 |
| <Sweep Time> 设置（ 64 位整型数） | 8575~8582 |
| <Sweep Run> 设置（ 8 位整型数） | 8583 |
| <Sineout Voltage> 设置（ 32 位浮点数） | 8592~8595 |
| <SweepMode> 设置（ 8 位整型数） | 8596 |
| <SweepSartVolt> 设置（ 32 位浮点数） | 8597~8600 |
| <SweepStopVolt> 设置（ 32 位浮点数） | 8601~8604 |
| <SweepStepVolt> 设置（ 32 位浮点数） | 8605~8608 |
| <SweepStepPrec> 设置（ 32 位浮点数） | 8609~8612 |
| <Sweep Time> 设置（ 64 位整型数） | 8613~8620 |
| <Sineout Sweep Run> 设置（ 8 位整型数） | 8621 |
| <Sineout DC Voltage> 设置（ 32 位浮点数） | 8622~8625 |


<!-- image -->


<!-- Page 85 -->

OE1022D DSP Lock-In Amplifier

79

| <Equation C1> 设置（ 64 位浮点数） | 8630~8637 |
|---|---|
| <Equation C2> 设置（ 64 位浮点数） | 8638~8645 |
| <Equation1 A> 源设置（ 8 位整型数） | 8646 |
| <Equation2 A> 源设置（ 8 位整型数） | 8647 |
| <Equation3 A> 源设置（ 8 位整型数） | 8648 |
| <Equation4 A> 源设置（ 8 位整型数） | 8649 |
| <Equation1 B> 源设置（ 8 位整型数） | 8650 |
| <Equation2 B> 源设置（ 8 位整型数） | 8651 |
| <Equation3 B> 源设置（ 8 位整型数） | 8652 |
| <Equation4 B> 源设置（ 8 位整型数） | 8653 |
| <Equation1 C> 源设置（ 8 位整型数） | 8654 |
| <Equation2 C> 源设置（ 8 位整型数） | 8655 |
| <Equation3 C> 源设置（ 8 位整型数） | 8656 |
| <Equation4 C> 源设置（ 8 位整型数） | 8657 |
| <Sensitivity> 设置（ 8 位整型数） | 8690 |
| <Reserve> 设置（ 8 位整型数） | 8691 |
| <Source> 设置（ 8 位整型数） | 8692 |
| <Grounding> 设置（ 8 位整型数） | 8693 |
| <Coupling> 设置（ 8 位整型数） | 8694 |
| <Line Notch> 设置（ 8 位整型数） | 8695 |
| <Time Constant> 设置（ 8 位整型数） | 8704 |
| <Filter dB/oct> 设置（ 8 位整型数） | 8705 |
| <Synchronous> 设置（ 8 位整型数） | 8706 |
| <Sample Time> 设置（ 64 位浮点数） | 8741~8748 |
| <Sample Length> 设置（ 64 位整型数） | 8749~8756 |
| <Sample Buffer1> 设置（ 8 位整型数） | 8757 |
| <Sample Buffer2> 设置（ 8 位整型数） | 8758 |
| <Sample Buffer3> 设置（ 8 位整型数） | 8759 |
| <Sample Buffer4> 设置（ 8 位整型数） | 8760 |
| <Sample Trigger Mode> 设置（ 8 位整型数） | 8761 |
| <Sample Mode> 设置（ 8 位整型数） | 8762 |
| <Sample Current Point> 设置 （ 64 位整型数） | 8763~8770 |
| Input Overload 状态（ 8 位整型数） | 8779 |
| Gain Overload 状态（ 8 位整型数） | 8780 |
| PLL LOCKED 状态（ 8 位整型数） IDN 序列号返回值（ 40Bytes 长度） | 8781 9170~9209 |


<!-- image -->


<!-- Page 86 -->

80

OE1022D DSP Lock-In Amplifier
