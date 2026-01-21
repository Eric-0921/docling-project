# TcpClient.h
automation, further development of the program is required.

        TcpClient.h
        #include <string>
        //defines structs for socket handling
        #include <netinet/in.h>
        using namespace std;
        typedef struct sockaddr_in  SockAddrStruct;
        typedef struct hostent     HostInfoStruct;
        class TcpClient
        {
          public:
            TcpClient();
            ~TcpClient();
            void connectToServer( string &hostname, int port );
            void disconnect( );
            void transmit( string &txString );
            void receive( string &rxString );
            string getCurrentHostName( ) const;
            int     getCurrentPort( ) const;
        private:
            string            currentHostName;
            int               currentPort;

Operating Manual 1407.0806.32 ─ 23

258

R&S ® SMB100A

Remote Control Basics

int                     currentSocketDescr;
        SockAddrStruct    serverAddress;
        HostInfoStruct * currentHostInfo;
        bool                clientIsConnected;
        int                     receiveBufferSize;
    };


