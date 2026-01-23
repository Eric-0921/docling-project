---
chapter_index: 1103
title: "Starting_a_Remote_Control_Session"
--- 

# Starting_a_Remote_Control_Session

Starting a Remote Control Session

SMB100A                                                             Remote Control Basics
                                                                                           Starting a Remote Control Session
                                                                                          
TcpClient::~TcpClient()
{
    currentHostInfo = NULL;
}


void TcpClient::connectToServer( string &hostname, int port )
{
    currentHostInfo = gethostbyname( hostname.c_str( ) );
    if( currentHostInfo == NULL )
    {
      currentHostName   = "";
      currentPort         = 0;
      currentHostInfo    = NULL;
      clientIsConnected = false;
      printf("error connecting host\n" );
    }
    currentHostName = hostname;
    currentPort      = port;
    currentSocketDescr = socket(AF_INET, SOCK_STREAM, 0);
    if( currentSocketDescr == 0 )
    {
      currentHostName   = "";
      currentPort         = 0;
      currentHostInfo    = NULL;
      clientIsConnected = false;
      printf("can't create socket\n" );
    }
    serverAddress.sin_family = currentHostInfo->h_addrtype;
    serverAddress.sin_port   = htons( currentPort );
    memcpy( ( char *) serverAddress.sin_addr.s_addr,
	currentHostInfo->h_addr_list[0], currentHostInfo->h_length );
    if( connect( currentSocketDescr, ( struct sockaddr *) &serverAddress,
	sizeof( serverAddress ) ) < 0 )
    {
      throw string("can't connect server\n" );
    }
    clientIsConnected = true;
  }
  void TcpClient::disconnect( )
  {
    if( clientIsConnected )
    {
      close( currentSocketDescr );
    }
    currentSocketDescr = 0;
    currentHostName      = "";
    currentPort          = 0;
    currentHostInfo      = NULL;
    clientIsConnected    = false;
  }


using Manual 1407.0806.32 -- 23
                                                                                           260

Operating Manual 1407.0806.32 ─ 23

260

R&S ® SMB100A

Remote Control Basics

