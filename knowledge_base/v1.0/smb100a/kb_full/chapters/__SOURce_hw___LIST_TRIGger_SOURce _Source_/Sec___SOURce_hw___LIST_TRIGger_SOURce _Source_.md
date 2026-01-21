# [:SOURce<hw>]:LIST:TRIGger:SOURce <Source>
Selects the trigger source processing lists.

The names of the parameters correspond to those under sweep mode. SCPI uses other names for the parameters; these names are also accepted by the instrument. The SCPI names should be used if compatibility is an important consideration. An overview of the various names is given in the following table:

| R&S name   | SCPI name   | Command under manual con- trol        |
|------------|-------------|---------------------------------------|
| AUTO       | IMMediate   | MODE AUTO                             |
| SINGle     | BUS         | MODE SINGLE or STEP                   |
| EXTernal   | EXTernal    | MODE EXT TRIG SINGLE or EXT TRIG STEP |
