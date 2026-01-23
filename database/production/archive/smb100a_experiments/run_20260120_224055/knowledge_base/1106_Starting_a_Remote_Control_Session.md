---
chapter_index: 1106
title: "Starting_a_Remote_Control_Session"
--- 

# Starting_a_Remote_Control_Session

Starting a Remote Control Session

<SMB100A
                                             Starring a Remote Control Basics
                                             Starring a Remote Control Session
    void printUsage()
    {
        cout<<"usage: EthernetRawCommand <server-ip> [scp-ip-command]"<<endl;
    }
    int main( int argc, char *argv[] )
    {
        int errorCode            = 0; // no error
        bool useSingleCommand = false;
        string singleCommand    = "";
        string hostname          = "";
        int     port             = 5025;
        string input            = "";
        TcpClient client;;
        switch( argc )
        {
            case 3:
                useSingleCommand = true;
                singleCommand     = argv[2];
            case 2:
                hostname          = argv[1];
                break;
            default:
                printUsage();
                return(-1);
        }
        try
        {
            client.connectToServer( hostname, port );
            bool terminate = false;
            while( !terminate )
            {
                char buffer[1024];
                if( useSingleCommand )
                {
                    input =  singleCommand; //send string
                }
                else
                {
                    cin.getline( buffer, 1024 );
                    input = buffer;
                    if( input == "end" )
                    {
                        terminate = true;
                    }
                }
                if( !terminate)
                {
                    client.transmit( input ); //send string
                    int qPos = input.find( "?", 0 );
                    //receive string only when needed


using Manual 1407.0806.32-- 23
                                                                                                      262

Operating Manual 1407.0806.32 ─ 23

262

R&S ® SMB100A

Remote Control Basics

if( qPos > 0 )
            {
                string rcStr = "";
                client.receive( rcStr );
                cout << rcStr << endl;
            }
        }
        if( useSingleCommand )
        {
            terminate = true;
        }
    }
}catch( const string errorString )
{
    cout<<errorString<<endl;
}
client.disconnect( );
return errorCode;
}



SCPII command structure

