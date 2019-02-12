a few common mistake,
1. get response "ActionNotSupported", it usually mean your url is not right check for example http://192.168.1.22/onvif/device_service should be PTZ or Media.
2. For name space, two needs to be considered, one is the namespace needs tab and enter, you might get the "tap not implemented" error.
3. "action not implemented" also means you should check namespace xmlns:soapenv something like this
4. Also pay attention to tt::Wiper|On or Wiper|On in different camera.
5. Sequence follows the get capabilities then get profiles then get nodes.
