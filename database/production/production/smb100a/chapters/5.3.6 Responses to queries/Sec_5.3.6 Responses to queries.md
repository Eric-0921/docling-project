# 5.3.6 Responses to queries
A query is defined for each setting command unless explicitly specified otherwise. It is formed by adding a question mark to the associated setting command. According to SCPI, the responses to queries are partly subject to stricter rules than in standard IEEE 488.2.

The requested parameter is transmitted without a header.

Maximum values, minimum values and all other quantities that are requested via a special text parameter are returned as numeric values.

Numeric values are output without a unit. Physical quantities are referred to the basic units or to the units set using the Unit command. The response 3.5E9 in the previous example stands for 3.5 GHz.

Truth values (Boolean values) are returned as 0 (for OFF) and 1 (for ON).

Example: HCOP:PAGE:ORI? Response: LAND

Example:

SENSe:FREQuency:STOP? MAX

Response: 3.5E9

