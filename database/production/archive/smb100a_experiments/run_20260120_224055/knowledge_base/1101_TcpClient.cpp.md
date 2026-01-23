---
chapter_index: 1101
title: "TcpClient.cpp"
--- 

# TcpClient.cpp

TcpClient.cpp

SockAddr struct     serverAddress;
                HostInfoStruct * currentHostInfo;
                bool                  clientIsConnected;
                int                  receiveBufferSize;
        };

        TcpClient.cpp
        #include <string>
        //defines structs for socket handling
        #include <netinet/in.h>
        using namespace std;
        typedef struct  sockaddr_in SockAddrStruct;
        typedef struct  hostent      HostInfoStruct;
        class TcpClient
        {
            public:
                TcpClient();
                ~TcpClient();
                void connectToServer( string &hostname, int port );
                void disconnect();
                void transmit( string &txString );
                void receive( string &rxString );
                string getCurrentHostName( ) const;
                int    getCurrentPort( ) const;
            private:
                string              currentHostName;
                int                  currentPort;
                int                  currentSocketDescr;
                SockAddrStruct     serverAddress;
                HostInfoStruct * currentHostInfo;
                bool                  clientIsConnected;
                int                  receiveBufferSize;
        };

        #include <netdb.h>
        #include <netinet/in.h>
        #include <unistd.h>
        #include "TcpClient.h"
        TcpClient::TcpClient()
        : currentHostName( "" )
        , currentPort( 0 )
        , currentSocketDescr( 0 )
        , serverAddress( )
        , currentHostInfo( NULL )
        , clientIsConnected( false )
        , receiveBufferSize( 1024 )
        {
        }



using Manual 1407.0806.32 -- 23

