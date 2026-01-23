---
chapter_index: 1104
title: "Starting_a_Remote_Control_Session"
--- 

# Starting_a_Remote_Control_Session

Starting a Remote Control Session

S&SMB100A                                                    Remote Control Basics
                                                    Starting a Remote Control Session

    void TcpClient::transmit( string &txString )
    {
      if( !clientIsConnected )
      {
		throw string("connection must be established before any data can be sent\n");
      }
      char * transmitBuffer = new char[txString.length() +1];
      memcpy( transmitBuffer, txString.c_str(), txString.length() );
      transmitBuffer[txString.length()] = '\n'; //newline is needed!
      if( send( currentSocketDescr, transmitBuffer, txString.length() + 1, 0 ) < 0 )
      {
        throw string("can't transmit data\n");
      }
      delete [] transmitBuffer;
    }
    void TcpClient::receive( string &rxString )
    {
      if( !clientIsConnected )
      {
		throw string("connection must be established before any data can be received\n");
      }
      char * receiveBuffer = new char[receiveBufferSize];
      memset( receiveBuffer, 0, receiveBufferSize );
      bool receiving = true;
      while( receiving )
      {
        int receivedByteCount = recv( currentSocketDescr,
        receiveBuffer, receiveBufferSize, 0 );
        if( receivedByteCount < 0 )
        {
          throw string("error while receiving data\n");
        }
        rxString += string( receiveBuffer );
        receiving = ( receivedByteCount == receiveBufferSize );
      }
      delete [] receiveBuffer;
    }
    string TcpClient::getCurrentHostName() const
    {
      return currentHostName;
    }
    int TcpClient::getCurrentPort() const
    {
      return currentPort;
    }

    TelnetClient.cpp
    #include <iostream>
    #include "TcpClient.h"

