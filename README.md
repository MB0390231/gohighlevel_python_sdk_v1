<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center" style="font-size: 50px">GoHighLevelSDK</h3>

  <p align="center">
    GoHighLevelSDK is a python package that provides an interface between your app and GoHighLevel's API.
    <br />
    <a href="https://github.com/MB0390231/GoHighLevelSDK/issues">Report Bug</a>
    ·
    <a href="https://github.com/MB0390231/GoHighLevelSDK/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This project was started to get accurate marketing information. I use python to connect various softwares without the use of expensive alternatives. GoHighLevel is one of the softwares I needed data from, so I decided to create a SDK to help others as well.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- Python

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Using this script is as simple.

1. Go to your GoHighLevel agency settings and copy your agency key.

2. Install the requirements using this command in the terminal.

```
pip install -r requirements.txt
```

3. Create a test.py file and copy the following code, making sure to add your agency key.

```
from GoHighLevelSDK.api import GoHighLevelAgency

agency_api_key = "<AGENCY KEY HERE>"

if __name__=="__main__":
    my_agency = GoHighLevel(agency_token=agency_api_key)

    locations = my_agency.get_locations()
    print(locations)
```

4. Run the test.py file.

Congrats! You are up and running :)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Email: michaelbroyles68@gmail.com\
Project Link: [GoHighLevelSDK](https://github.com/MB0390231/GoHighLevelSDK)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/MB0390231/GoHighLevelSDK.svg?style=for-the-badge
[contributors-url]: https://github.com/MB0390231/GoHighLevelSDK/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/MB0390231/GoHighLevelSDK.svg?style=for-the-badge
[forks-url]: https://github.com/MB0390231/GoHighLevelSDK/network/meMBers
[stars-shield]: https://img.shields.io/github/stars/MB0390231/GoHighLevelSDK.svg?style=for-the-badge
[stars-url]: https://github.com/MB0390231/GoHighLevelSDK/stargazers
[issues-shield]: https://img.shields.io/github/issues/MB0390231/GoHighLevelSDK.svg?style=for-the-badge
[issues-url]: https://github.com/MB0390231/GoHighLevelSDK/issues
[license-shield]: https://img.shields.io/github/license/MB0390231/GoHighLevelSDK.svg?style=for-the-badge
[license-url]: https://github.com/MB0390231/GoHighLevelSDK/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/michael-broyles-4634b2195
[product-screenshot]: images/preview.png
