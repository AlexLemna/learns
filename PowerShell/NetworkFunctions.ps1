Function Get-ComputerIPinfo
{
    $IP = Get-WmiObject -Class Win32_NetworkAdapterConfiguration -Filter "IPEnabled = $true"
    "IP Address: " + $IP.IPAddress[0]
    "Subnet Mask: " + $IP.IPSubnet[0]
    "Gateway: " + $IP.DefaultIPGateway
    "DNS Server #1: " + $IP.DNSServerSearchOrder[0]
    "DNS Server #2: " + $IP.DNSServerSearchOrder[1]
    "FQDN: " + $IP.DNSHostName + "." + $IP.DNSDomain
} # End Get-ComputerIPinfo