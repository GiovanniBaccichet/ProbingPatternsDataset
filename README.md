<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/GiovanniBaccichet/ProbingPatternsDataset">
    <img src="images/satellite-antenna.png" alt="Logo" width="120">
  </a>

<h3 align="center">Probe Requests Open Dataset</h3>

  <p align="center">
    MAC Address De-Randomization using Multi-Channel Sniffers and Two-Stage Clustering
    <br />
    <br />
    <a href="https://github.com/GiovanniBaccichet/ProbingPatternsDataset/issues">Report Bug</a>
    ·
    <a href="https://github.com/GiovanniBaccichet/ProbingPatternsDataset/issues">Request Feature</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

Wi-Fi Probe Request captures of different devices, most of which share the *Operating System* (OS) version and (or) the model. The captures were performed using 3x ALFA `AWUS036ACS`, set respectively to channel 1, 6 and 11 of the 2.4 GHz spectrum. The driver used was an [open source one](https://github.com/morrownr/8821au-20210708) for the Realtek `RTL8812AU` chipset. 

| Device                   | OS            | Identifier      | Mode  | Faraday Bag |
|--------------------------|---------------|-----------------|-------|-------------|
| Apple iPhone 12 Pro      | iOS `16.4.1(a)` | `iPhone12Pro-C`   | PA, S | I           |
| Apple iPhone 12          | iOS `16.4.1(a)` | `iPhone12-M`      | A, S  | I           |
| Apple iPhone 11          | iOS `16.4.1(a)` | `iPhone11-B`      | A, S  | I           |
| Apple iPhone 11          | iOS `16.4.1(a)` | `iPhone11-C`      | A, S  | I           |
| Apple iPhone 11          | iOS `16.4.1(a)` | `iPhone11-F`      | A, S  | I           |
| Apple iPhone 11          | iOS `16.4.1(a)` | `iPhone11-M`      | A, S  | I           |
| Apple iPhone XR          | iOS `16.4.1(a)` | `iPhoneXR-A`      | A, S  | I           |
| Apple iPhone XR          | iOS `16.4.1(a)` | `iPhoneXR-L`      | A, S  | I           |
| Apple iPhone 7           | iOS `15.5`      | `iPhone7-F`       | A, S  | I           |
| Samsung Galaxy S21 Ultra | Android `13`    | `S21Ultra-M`      | A, S  | I           |
| Oppo Find X3 Neo         | Android `13`    | `OppoFindX3Neo-A` | S     | I           |

To ensure user privacy, the data in the PCAP files has undergone anonymization processes.

The following steps have been taken to anonymize sensitive information:

- **MAC Address Anonymization**: Original MAC addresses have been replaced with randomly generated MAC addresses, ensuring that identical (original) MAC addresses have identical random counterparts.
- **SSID Anonymization**: SSID information has been hashed using a secure hash function. The length of the hashed SSID matches the length of the original SSID to prevent malformed packets.

The script used to perform said process is included in the repository, and called `PCAP_anonymizer.py` and requires `scapy` to run.


<p align="right">(<a href="#readme-top">back to top</a>)</p>