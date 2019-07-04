from enum import Enum
from typing import NamedTuple

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


class Severity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    BEST_PRACTICE = "best_practice"
    INFO = "info"


class VulnerabilityInfoBase(NamedTuple):
    name: str
    severity: Severity
    description: str
    display_all: bool = False
    id: str = None  # must be the last item


class VulnerabilityInfo(VulnerabilityInfoBase):
    def __new__(cls, *args, **kwargs):
        base = super().__new__(cls, *args, **kwargs)
        data = list(base)

        # if the last item is none, replace with a generated ID
        # if it isn't none, leave it alone - this allows for manual values
        if data[-1] is None:
            digest = hashes.Hash(hashes.SHAKE128(5), backend=default_backend())
            digest.update(args[0].encode("utf_8"))
            d = digest.finalize().hex()
            id_val = f"Y{d}"

            data.pop(-1)
            data.append(id_val)

            self = super().__new__(cls, *tuple(data))
        else:
            self = base

        return self


class VulnerabilityInfoEnum(VulnerabilityInfo, Enum):
    pass


class Vulnerabilities(VulnerabilityInfoEnum):
    APP_WORDPRESS_VERSION = VulnerabilityInfo("App_WordPress_Version", Severity.LOW, "")
    APP_WORDPRESS_OUTDATED = VulnerabilityInfo(
        "App_WordPress_Outdated", Severity.MEDIUM, ""
    )
    APP_WORDPRESS_USER_ENUM_API = VulnerabilityInfo(
        "App_WordPress_User_Enum_API", Severity.MEDIUM, ""
    )
    APP_WORDPRESS_USER_FOUND = VulnerabilityInfo(
        "App_WordPress_User_Found", Severity.LOW, "", True
    )

    COOKIE_MISSING_SECURE_FLAG = VulnerabilityInfo(
        "Cookie_Missing_Secure_Flag", Severity.MEDIUM, ""
    )
    COOKIE_MISSING_HTTPONLY_FLAG = VulnerabilityInfo(
        "Cookie_Missing_HttpOnly_Flag", Severity.LOW, ""
    )
    COOKIE_MISSING_SAMESITE_FLAG = VulnerabilityInfo(
        "Cookie_Missing_SameSite_Flag", Severity.BEST_PRACTICE, ""
    )
    COOKIE_WITH_SAMESITE_NONE_FLAG = VulnerabilityInfo(
        "Cookie_With_SameSite_None_Flag", Severity.BEST_PRACTICE, ""
    )
    COOKIE_INVALID_SECURE_FLAG = VulnerabilityInfo(
        "Cookie_Invalid_Secure_Flag", Severity.MEDIUM, ""
    )
    COOKIE_INVALID_SAMESITE_NONE_FLAG = VulnerabilityInfo(
        "Cookie_Invalid_SameSite_None_Flag", Severity.LOW, ""
    )

    DNS_CAA_MISSING = VulnerabilityInfo("Dns_CAA_Missing", Severity.LOW, "")
    DNS_DNSSEC_NOT_ENABLED = VulnerabilityInfo(
        "Dns_DNSSEC_Not_Enabled", Severity.BEST_PRACTICE, ""
    )

    JS_VULNERABLE_VERSION = VulnerabilityInfo(
        "Js_Vulnerable_Version", Severity.MEDIUM, "", True
    )
    JS_EXTERNAL_FILE = VulnerabilityInfo("Js_External_File", Severity.LOW, "", True)

    HTTP_BANNER_GENERIC_APACHE = VulnerabilityInfo(
        "Http_Banner_Generic_Apache", Severity.INFO, ""
    )
    HTTP_BANNER_APACHE_VERSION = VulnerabilityInfo(
        "Http_Banner_Apache_Version", Severity.LOW, ""
    )
    HTTP_BANNER_GENERIC_NGINX = VulnerabilityInfo(
        "Http_Banner_Generic_Nginx", Severity.INFO, ""
    )
    HTTP_BANNER_NGINX_VERSION = VulnerabilityInfo(
        "Http_Banner_Nginx_Version", Severity.LOW, ""
    )
    HTTP_BANNER_PYTHON_VERSION = VulnerabilityInfo(
        "Http_Banner_Python_Version", Severity.LOW, ""
    )
    HTTP_BANNER_IIS_VERSION = VulnerabilityInfo(
        "Http_Banner_IIS_Version", Severity.LOW, ""
    )
    HTTP_BANNER_OPENSSL_VERSION = VulnerabilityInfo(
        "Http_Banner_OpenSSL_Version", Severity.LOW, ""
    )
    HTTP_PHP_VERSION_EXPOSED = VulnerabilityInfo(
        "Http_PHP_Version_Exposed", Severity.LOW, ""
    )

    HTTP_HEADER_CONTENT_SECURITY_POLICY_MISSING = VulnerabilityInfo(
        "Http_Header_Content_Security_Policy_Missing", Severity.LOW, ""
    )
    HTTP_HEADER_CORS_ACAO_UNRESTRICTED = VulnerabilityInfo(
        "Http_Header_CORS_ACAO_Unrestricted", Severity.LOW, ""
    )
    HTTP_HEADER_FEATURE_POLICY_MISSING = VulnerabilityInfo(
        "Http_Header_Feature_Policy_Missing", Severity.BEST_PRACTICE, ""
    )
    HTTP_HEADER_HSTS_MISSING = VulnerabilityInfo(
        "Http_Hsts_Missing", Severity.MEDIUM, ""
    )
    HTTP_HEADER_REFERRER_POLICY_MISSING = VulnerabilityInfo(
        "Http_Header_Referrer_Policy_Missing", Severity.BEST_PRACTICE, ""
    )
    HTTP_HEADER_VIA = VulnerabilityInfo("Http_Header_Via", Severity.BEST_PRACTICE, "")
    HTTP_HEADER_X_BACKEND_SERVER = VulnerabilityInfo(
        "Http_Header_X_Backend_Server", Severity.BEST_PRACTICE, ""
    )
    HTTP_HEADER_X_CONTENT_TYPE_OPTIONS_MISSING = VulnerabilityInfo(
        "Http_Header_X_Content_Type_Options_Missing", Severity.LOW, ""
    )
    HTTP_HEADER_X_FRAME_OPTIONS_ALLOW = VulnerabilityInfo(
        "Http_Header_X_Frame_Options_Allow", Severity.LOW, ""
    )
    HTTP_HEADER_X_FRAME_OPTIONS_MISSING = VulnerabilityInfo(
        "Http_Header_X_Frame_Options_Missing", Severity.LOW, ""
    )
    HTTP_HEADER_X_POWERED_BY = VulnerabilityInfo(
        "Http_Header_X_Powered_By", Severity.BEST_PRACTICE, ""
    )
    HTTP_HEADER_X_RUNTIME = VulnerabilityInfo(
        "Http_Header_X_Runtime", Severity.BEST_PRACTICE, ""
    )
    HTTP_HEADER_X_XSS_PROTECTION_DISABLED = VulnerabilityInfo(
        "Http_Header_X_Xss_Protection_Disabled", Severity.LOW, ""
    )
    HTTP_HEADER_X_XSS_PROTECTION_MISSING = VulnerabilityInfo(
        "Http_Header_X_Xss_Protection_Missing", Severity.LOW, ""
    )
    HTTP_HEADER_X_ASPNETMVC_VERSION = VulnerabilityInfo(
        "Http_X_AspNetMvc_Version", Severity.LOW, ""
    )
    HTTP_HEADER_X_ASPNET_VERSION = VulnerabilityInfo(
        "Http_X_AspNet_Version", Severity.LOW, ""
    )
    HTTP_HEADER_CONTENT_TYPE_NO_CHARSET = VulnerabilityInfo(
        "Http_Header_Content_Type_No_Charset", Severity.LOW, ""
    )
    HTTP_HEADER_CONTENT_TYPE_MISSING = VulnerabilityInfo(
        "Http_Header_Content_Type_Missing", Severity.LOW, ""
    )
    HTTP_ERROR_MESSAGE = VulnerabilityInfo(
        "Http_Error_Message", Severity.MEDIUM, "", True
    )
    HTTP_INSECURE_LINK = VulnerabilityInfo("Http_Insecure_Link", Severity.LOW, "", True)
    HTTP_PROPFIND_ENABLED = VulnerabilityInfo("Http_Propfind_Enabled", Severity.LOW, "")
    HTTP_TRACE_ENABLED = VulnerabilityInfo("Http_Trace_Enabled", Severity.LOW, "")
    HTTP_OPTIONS_ALLOW = VulnerabilityInfo("Http_Option_Allow", Severity.INFO, "")
    HTTP_OPTIONS_PUBLIC = VulnerabilityInfo("Http_Option_Public", Severity.INFO, "")

    TLS_CBC_CIPHER_SUITE = VulnerabilityInfo(
        "Tls_CBC_Cipher_Suite", Severity.BEST_PRACTICE, ""
    )

    TLS_CERT_BAD_COMMON_NAME = VulnerabilityInfo(
        "Tls_Cert_Bad_Common_Name", Severity.HIGH, ""
    )
    TLS_CERT_BLACKLISTED = VulnerabilityInfo("Tls_Cert_Blacklisted", Severity.HIGH, "")
    TLS_CERT_EXPIRED = VulnerabilityInfo("Tls_Cert_Expired", Severity.HIGH, "")
    TLS_CERT_HOSTNAME_MISMATCH = VulnerabilityInfo(
        "Tls_Cert_Hostname_Mismatch", Severity.HIGH, ""
    )
    TLS_CERT_INSECURE_KEY = VulnerabilityInfo(
        "Tls_Cert_Insecure_Key", Severity.HIGH, ""
    )
    TLS_CERT_INSECURE_SIGNATURE = VulnerabilityInfo(
        "Tls_Cert_Insecure_Signature", Severity.HIGH, ""
    )
    TLS_CERT_NOT_YET_VALID = VulnerabilityInfo(
        "Tls_Cert_Not_Yet_Valid", Severity.HIGH, ""
    )
    TLS_CERT_NO_TRUST = VulnerabilityInfo("Tls_Cert_No_Trust", Severity.HIGH, "")
    TLS_CERT_REVOKED = VulnerabilityInfo("Tls_Cert_Revoked", Severity.HIGH, "")
    TLS_CERT_SELF_SIGNED = VulnerabilityInfo("Tls_Cert_Self_Signed", Severity.HIGH, "")

    TLS_COMPRESSION_ENABLED = VulnerabilityInfo(
        "Tls_Compression_Enabled", Severity.HIGH, ""
    )
    TLS_DH_KNOWN_PRIMES_STRONG = VulnerabilityInfo(
        "Tls_DH_Known_Primes_Strong", Severity.MEDIUM, ""
    )
    TLS_DH_KNOWN_PRIMES_WEAK = VulnerabilityInfo(
        "Tls_DH_Known_Primes_Weak", Severity.HIGH, ""
    )
    TLS_DH_PARAM_REUSE = VulnerabilityInfo("Tls_DH_Param_Reuse", Severity.LOW, "")
    TLS_DROWN = VulnerabilityInfo("Tls_Drown", Severity.MEDIUM, "")
    TLS_ECDH_PARAM_REUSE = VulnerabilityInfo("Tls_ECDH_Param_Reuse", Severity.LOW, "")
    TLS_FALLBACK_SCSV_MISSING = VulnerabilityInfo(
        "Tls_Fallback_SCSV_Missing", Severity.LOW, ""
    )
    TLS_FREAK = VulnerabilityInfo("Tls_Freak", Severity.HIGH, "")
    TLS_GOLDENDOODLE = VulnerabilityInfo("Tls_Goldendoodle", Severity.HIGH, "")
    TLS_GOLDENDOODLE_NE = VulnerabilityInfo("Tls_Goldendoodle_NE", Severity.MEDIUM, "")
    TLS_HEARTBEAT_ENABLED = VulnerabilityInfo(
        "Tls_Heartbeat_Enabled", Severity.BEST_PRACTICE, ""
    )
    TLS_HEARTBLEED = VulnerabilityInfo("Tls_Heartbleed", Severity.CRITICAL, "")
    TLS_INSECURE_CIPHER_SUITE = VulnerabilityInfo(
        "Tls_Insecure_Cipher_Suite", Severity.MEDIUM, ""
    )
    TLS_INSECURE_RENEG = VulnerabilityInfo("Tls_Insecure_Reneg", Severity.HIGH, "")
    TLS_LEGACY_SSL_ENABLED = VulnerabilityInfo(
        "Tls_Legacy_SSL_Enabled", Severity.HIGH, ""
    )
    TLS_LEGACY_SSL_POODLE = VulnerabilityInfo(
        "Tls_Legacy_SSL_Poodle", Severity.HIGH, ""
    )
    TLS_LIMITED_FORWARD_SECRECY = VulnerabilityInfo(
        "Tls_Limited_Forward_Secrecy", Severity.LOW, ""
    )
    TLS_LOGJAM = VulnerabilityInfo("Tls_Logjam", Severity.HIGH, "")
    TLS_NO_AEAD_SUPPORT = VulnerabilityInfo(
        "Tls_No_AEAD_Support", Severity.BEST_PRACTICE, ""
    )
    TLS_OCSP_STAPLE_MISSING = VulnerabilityInfo(
        "Tls_OCSP_Staple_Missing", Severity.LOW, ""
    )

    TLS_OPENSSL_CVE_2014_0224 = VulnerabilityInfo(
        "Tls_OpenSSL_CVE_2014_0224", Severity.HIGH, ""
    )
    TLS_OPENSSL_CVE_2014_0224_NE = VulnerabilityInfo(
        "Tls_OpenSSL_CVE_2014_0224_NE", Severity.MEDIUM, ""
    )
    TLS_OPENSSL_CVE_2016_2107 = VulnerabilityInfo(
        "Tls_OpenSSL_CVE_2016_2107", Severity.HIGH, ""
    )
    TLS_OPENSSL_CVE_2019_1559 = VulnerabilityInfo(
        "Tls_OpenSSL_CVE_2019_1559", Severity.HIGH, ""
    )
    TLS_OPENSSL_CVE_2019_1559_NE = VulnerabilityInfo(
        "Tls_OpenSSL_CVE_2019_1559_NE", Severity.MEDIUM, ""
    )

    TLS_POODLE = VulnerabilityInfo("Tls_Poodle", Severity.HIGH, "")
    TLS_ROBOT_ORACLE_STRONG = VulnerabilityInfo(
        "Tls_Robot_Oracle_Strong", Severity.MEDIUM, ""
    )
    TLS_ROBOT_ORACLE_WEAK = VulnerabilityInfo("Tls_Robot_Oracle_Weak", Severity.LOW, "")
    TLS_SESSION_RESP_ENABLED = VulnerabilityInfo(
        "Tls_Session_Resp_Enabled", Severity.BEST_PRACTICE, ""
    )
    TLS_SLEEPING_POODLE = VulnerabilityInfo("Tls_Sleeping_Poodle", Severity.HIGH, "")
    TLS_SLEEPING_POODLE_NE = VulnerabilityInfo(
        "Tls_Sleeping_Poodle_NE", Severity.MEDIUM, ""
    )
    TLS_SWEET32 = VulnerabilityInfo("Tls_SWEET32", Severity.HIGH, "")
    TLS_SYMANTEC_ROOT = VulnerabilityInfo("Tls_Symantec_Root", Severity.HIGH, "")
    TLS_TICKETBLEED = VulnerabilityInfo("Tls_Ticketbleed", Severity.HIGH, "")

    TLS_VERSION_1_0_ENABLED = VulnerabilityInfo(
        "Tls_Version_1_0_Enabled", Severity.LOW, ""
    )
    TLS_VERSION_1_3_EARLY_DATA_ENABLED = VulnerabilityInfo(
        "Tls_Version_1_3_Early_Data_Enabled", Severity.BEST_PRACTICE, ""
    )
    TLS_VERSION_1_3_NOT_ENABLED = VulnerabilityInfo(
        "Tls_Version_1_3_Not_Enabled", Severity.BEST_PRACTICE, ""
    )

    TLS_ZOMBIE_POODLE = VulnerabilityInfo("Tls_Zombie_Poodle", Severity.HIGH, "")
    TLS_ZOMBIE_POODLE_NE = VulnerabilityInfo(
        "Tls_Zombie_Poodle_NE", Severity.MEDIUM, ""
    )

    SERVER_APACHE_OUTDATED = VulnerabilityInfo(
        "Server_Apache_Outdated", Severity.MEDIUM, ""
    )
    SERVER_APACHE_STATUS = VulnerabilityInfo(
        "Server_Apache_Status", Severity.MEDIUM, ""
    )
    SERVER_APACHE_INFO = VulnerabilityInfo("Server_Apache_Info", Severity.MEDIUM, "")
    SERVER_TOMCAT_VERSION = VulnerabilityInfo(
        "Server_Tomcat_Version", Severity.MEDIUM, ""
    )
    SERVER_TOMCAT_OUTDATED = VulnerabilityInfo(
        "Server_Tomcat_Outdated", Severity.MEDIUM, ""
    )
    SERVER_TOMCAT_MANAGER_EXPOSED = VulnerabilityInfo(
        "Server_Tomcat_Manager_Exposed", Severity.HIGH, ""
    )
    SERVER_TOMCAT_HOST_MANAGER_EXPOSED = VulnerabilityInfo(
        "Server_Tomcat_Host_Manager_Exposed", Severity.HIGH, ""
    )
    SERVER_TOMCAT_MANAGER_WEAK_PASSWORD = VulnerabilityInfo(
        "Server_Tomcat_Manager_Weak_Password", Severity.CRITICAL, "", True
    )
    SERVER_TOMCAT_CVE_2017_12615 = VulnerabilityInfo(
        "Server_Tomcat_CVE_2017_12615", Severity.CRITICAL, ""
    )
    SERVER_TOMCAT_CVE_2019_0232 = VulnerabilityInfo(
        "Server_Tomcat_CVE_2019_0232", Severity.CRITICAL, ""
    )
    SERVER_TOMCAT_STRUTS_SAMPLE = VulnerabilityInfo(
        "Server_Tomcat_Struts_Sample", Severity.LOW, "", True
    )
    SERVER_NGINX_OUTDATED = VulnerabilityInfo(
        "Server_Nginx_Outdated", Severity.MEDIUM, ""
    )
    SERVER_NGINX_STATUS_EXPOSED = VulnerabilityInfo(
        "Server_Nginx_Status_Exposed", Severity.LOW, ""
    )
    SERVER_PHP_OUTDATED = VulnerabilityInfo("Server_PHP_Outdated", Severity.MEDIUM, "")
    SERVER_IIS_OUTDATED = VulnerabilityInfo("Server_IIS_Outdated", Severity.MEDIUM, "")
    SERVER_ASPNETMVC_OUTDATED = VulnerabilityInfo(
        "Server_AspNetMvc_Outdated", Severity.MEDIUM, ""
    )
    SERVER_ASPNET_OUTDATED = VulnerabilityInfo(
        "Server_AspNet_Outdated", Severity.MEDIUM, ""
    )
    SERVER_ASPNET_DEBUG_ENABLED = VulnerabilityInfo(
        "Server_AspNet_Debug_Enabled", Severity.HIGH, ""
    )
    SERVER_ASPNET_HANDLER_ENUM = VulnerabilityInfo(
        "Server_AspNet_Handler_Enum", Severity.LOW, "", True
    )
    SERVER_RAILS_CVE_2019_5418 = VulnerabilityInfo(
        "Server_Rails_CVE_2019_5418", Severity.CRITICAL, ""
    )
    SERVER_INVALID_404_FILE = VulnerabilityInfo(
        "Server_Invalid_404_File", Severity.INFO, ""
    )
    SERVER_INVALID_404_PATH = VulnerabilityInfo(
        "Server_Invalid_404_Path", Severity.INFO, ""
    )
    SERVER_SPECIAL_FILE_EXPOSED = VulnerabilityInfo(
        "Server_Special_File_Exposed", Severity.INFO, "", True
    )
    SERVER_INT_IP_EXP_HTTP10 = VulnerabilityInfo(
        "Server_Int_IP_Exp_Http10", Severity.LOW, ""
    )

    WAF_CLOUDFLARE = VulnerabilityInfo("Waf_Cloudflare", Severity.INFO, "")
    WAF_INCAPSULA = VulnerabilityInfo("Waf_Incapsula", Severity.INFO, "")
