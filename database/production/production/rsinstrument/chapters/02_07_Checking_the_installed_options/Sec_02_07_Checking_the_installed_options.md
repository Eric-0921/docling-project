# Checking the installed options[](#checking-the-installed-options "Link to this heading")

If your instrument refuses to execute desired actions, and you do not know why - after all, the SCPI commands are in the User Manual, it’s worth to check if the a special option is required.
RsInstrument provides several ways to do it. The following example shows the literal CASE-INSENSITIVE searching:

```python
 1"""
 2Checking the installed options with literal search.
 3"""
 4
 5from RsInstrument import *
 6
 7instr = RsInstrument('TCPIP::192.168.56.101::hislip0')
 8
 9# Get all the options as list, and check for the specific one.
10if 'K1' in instr.instrument_options:
11	print('Option K1 installed')
12
13# Check for one option.
14# Keep in mind, that if the 'K0' is present, all the K-options are reported as installed.
15if instr.has_instr_option('K1'):
16	print('Option K1 installed')
17	
18# Check whether the K0 is installed:
19if instr.has_instr_option_k0():
20	print('You are a lucky customer, your instrument has all the K-options available.')
21	
22# Check with a dedicated function for at least one option (logical OR).
23if instr.has_instr_option('K1 / K1a / K1b'):
24	print('At least one of the K1,K1a,K1b installed')
25
26# Same as previous, but entered as a list of strings.
27if instr.has_instr_option(['K1', 'K1a', 'K1b']):
28	print('At least one of the K1,K1a,K1b installed')
29
30instr.close()
```

Note

`instr.instrument_options` returns neatly sorted list of options, where the duplicates are removed, K-options are at the beginning, and the B-options at the end.

If for any reason you want to see how many times the K101 option was in the original Option’s string, use the `io.get_option_counts('K101')`

Regular expressions CASE-INSENSITIVE searching. The Regex must be fully matched. That means, for example, `K1.` only positively matches `K10` or `K17`, but not `K1` or `K110`

```python
 1"""
 2Checking the installed options with regular expressions search.
 3"""
 4
 5from RsInstrument import *
 6
 7instr = RsInstrument('TCPIP::192.168.56.101::hislip0')
 8
 9# Check for one option.
10# Keep in mind, that if the 'K0' is present, all the K-options are reported as installed.
11if instr.has_instr_option_regex('K1.'):
12    print('Option K10 or K11 or K12 up to K19 installed')
13
14# Check with a dedicated function for at least one option (logical OR).
15if instr.has_instr_option_regex('K1. / K2..'):
16    print('At least one of the K10..K19, K200..K299 installed')
17
18# Same as previous, but entered as a list of strings.
19if instr.has_instr_option_regex(['K1.', 'K2..']):
20    print('At least one of the K10..K19, K200..K299 installed')
21
22instr.close()
```

If you wish to add or remove reported options, you can use `add_instr_option()` or `remove_instr_option()`. The `instr.instrument_options` is re-sorted after each change in the list:

```python
 1"""
 2Changing how the installed options are reported.
 3This code does not actually install any option on the instrument :-)
 4"""
 5
 6from RsInstrument import *
 7
 8instr = RsInstrument('TCPIP::192.168.56.101::hislip0')
 9
10# I want to remove the 'K0' and see if the individual K-options are reported as present.
11instr.remove_instr_option('K0')
12if not instr.has_instr_option_k0():
13    print('We have lost the K0, let us hope the individual options are still reported.')
14
15instr.add_instr_option('K0')
16if not instr.has_instr_option_k0():
17    print('Now we have the K0 again :-)')
```

Note

It would be nice to install an instrument option with this small python script. Unfortunately, this is not the case - the script just manipulates the reported list of options. If you want to install an option on your instrument, you will have to buy it :-)
