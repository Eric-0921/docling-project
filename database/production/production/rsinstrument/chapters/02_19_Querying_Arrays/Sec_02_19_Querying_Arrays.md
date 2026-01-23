# Querying Arrays[](#querying-arrays "Link to this heading")

Often you need to query an array of numbers from your instrument, for example a spectrum analyzer trace or an oscilloscope waveform.
Many programmers stick to transferring such arrays in ASCII format, because of the simplicity. Although simple, it is quite inefficient: one float 32-bit number can take up to 12 characters (bytes), compared to 4 bytes in a binary form. Well, with RsInstrument do not worry about the complexity: we have one method for binary or ascii array transfer.
