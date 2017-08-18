from pyzenvia.enums import APIVersion

URLS = {
    APIVersion.V1: {
        "debug": {
            "send": ''
        },
        "production": {
            "send": 'http://www.zenvia360.com.br/GatewayIntegration/msgSms.do?dispatch=send'
        }
    },
    APIVersion.V2: {
        "debug": {
            "send": ''
        },
        "production": {
            "send": ''
        }
    }
}
