#import xml.etree.cElementTree as ElementTree

import requests
import untangle

NAMESILO_OPERATIONS = {
    'add_account_funds': 'addAccountFunds',
    'add_auto_renew': 'addAutoRenewal',
    'add_contact': 'contactAdd',
    'add_dns_record': 'dnsAddRecord',
    'add_email_forward': 'configureEmailForward',
    'add_portfolio': 'portfolioAdd',
    'add_privacy': 'addPrivacy',
    'add_registered_nameserver': 'addRegisteredNameServer',
    'associate_contact': 'contactDomainAssociate',
    'associate_portfolio': 'portfolioDomainAssociate',
    'change_nameservers': 'changeNameServers',
    'check_register_availability': 'checkRegisterAvailability',
    'check_transfer_availability': 'checkTransferAvailability',
    'check_transfer_status': 'checkTransferStatus',
    'delete_dns_record': 'dnsUpdateRecord',
    'delete_portfolio': 'portfolioDelete',
    'delete_registered_nameserver': 'deleteRegisteredNameServer',
    'forward_domain': 'domainForward',
    'get_account_balance': 'getAccountBalance',
    'get_auth_code': 'retrieveAuthCode',
    'get_domain_info': 'getDomainInfo',
    'list_contacts': 'contactList',
    'list_dns_records': 'dnsListRecords',
    'list_domains': 'listDomains',
    'list_email_forwards': 'listEmailForwards',
    'list_portfolios': 'portfolioList',
    'list_registered_nameservers': 'listRegisteredNameServers',
    'lock_domain': 'domainLock',
    'register_domain': 'registerDomain',
    'renew_domain': 'renewDomain',
    'remove_auto_renewal': 'removeAutoRenewal',
    'remove_email_forward': 'deleteEmailForward',
    'remove_privacy': 'removePrivacy',
    'transfer_domain': 'ransferDomain',
    'unlock_domain': 'domainUnlock',
    'update_contact': 'contactUpdate',
    'update_dns_record': 'dnsUpdateRecord',
    'update_portfolio': 'portfoliopdate',
    'update_registered_nameserver': 'modifyRegisteredNameServer',
    'update_registered_nameserver': 'updateRegisteredNameServer'
}


class NameSiloError(Exception):
    """Base class for NameSilo errors."""
    pass


class HTTPSNotUsed(NameSiloError):
    """Raised if request is made without HTTPS."""
    pass


class NoVersionSpecified(NameSiloError):
    """Raised if no version is specified in the request."""
    pass


class InvalidAPIVersion(NameSiloError):
    """Raised if the ApI version specified is invalid."""
    pass


class NoTypeSpecified(NameSiloError):
    """Raised if no type is specified in request."""
    pass


class InvalidAPIType(NameSiloError):
    """Raised if API type is invalid."""
    pass


class NoOperationSpecified(NameSiloError):
    """Raised if no operation is specified in request."""
    pass


class issingAPIParameters(NameSiloError):
    """Raised if there are missing parameters for the specified operation."""
    pass


class InvalidAPIOperation(NameSiloError):
    """Raised if the API operaiton is invalid."""
    pass


class MissingOperationParameters(NameSiloError):
    """Raised if parameters are missing from the API operation."""
    pass


class NoAPIKeySpecified(NameSiloError):
    """Raised if no API key is specified for request."""
    pass


class InvalidAPIKey(NameSiloError):
    """Raised if the API key is invalid."""
    pass


class InvalidUser(NameSiloError):
    """Raised if user associatedwith API key is invalid."""
    pass


class APINotAvailableToSubAccounts(NameSiloError):
    pass


class invalidIPAddress(NameSiloError):
    pass


class InvalidDomainSyntax(NameSiloError):
    pass


class CentralRegistryNotResponding(NameSiloError):
    pass


class InvalidSandboxAccount(NameSiloError):
    pass


class CreditCardProfileDoesNotExist(NameSiloError):
    pass


class UnverifiedCreditCardProfile(NameSiloError):
    pass


class InsufficientAccountFunds(NameSiloError):
    pass


class ApIKeyNotPassedasGet(NameSiloError):
    pass


class DomainNotActive(NameSiloError):
    pass


class InteralSystemError(NameSiloError):
    pass


class DomainAlreadyAutoRenew(NameSiloError):
    pass


class DomainAlreadyNotAutoReview(NameSiloError):
    pass


class DomainAlreadyLocked(NameSiloError):
    pass


class DomainAlreadyUnlocked(NameSiloError):
    pass


class NameserverUpdateError(NameSiloError):
    pass


class DomainAlreadyPrivate(NameSiloError):
    pass


class DomainAlreadyNotPrivate(NameSiloError):
    pass


class ProcessingError(NameSiloError):
    pass


class DomainAlreadyActive(NameSiloError):
    pass


class InvalidNumberOfYears(NameSiloError):
    pass


class DomainRenewalError(NameSiloError):
    pass


class DomainTransferError(NameSiloError):
    pass


class DomainTransferDoesNotExist(NameSiloError):
    pass


class InvalidDomainName(NameSiloError):
    pass


class DNSModificationErrror(NameSiloError):
    pass


NAMESILO_ERRORS = { 
    '101': HTTPSNotUsed,
    '102': NoVersionSpecified,
    '103': InvalidAPIVersion,
    '104': NoTypeSpecified,
    '105': InvalidAPIType,
    '106': NoOperationSpecified,
    '107': InvalidAPIOperation,
    '108': MissingOperationParameters,
    '109': NoAPIKeySpecified,
    '110': InvalidAPIKey,
    '111': InvalidUser,
    '112': APINotAvailableToSubAccounts,
    '113': invalidIPAddress,
    '114': InvalidDomainSyntax,
    '115': CentralRegistryNotResponding,
    '116': InvalidSandboxAccount,
    '117': CreditCardProfileDoesNotExist,
    '118': UnverifiedCreditCardProfile,
    '119': InsufficientAccountFunds,
    '120': ApIKeyNotPassedasGet,
    '200': DomainNotActive,
    '201': InteralSystemError,
    '210': NameSiloError,
    '250': DomainAlreadyAutoRenew,
    '251': DomainAlreadyNotAutoReview,
    '252': DomainAlreadyLocked,
    '253': DomainAlreadyUnlocked,
    '254': NameserverUpdateError,
    '255': DomainAlreadyPrivate,
    '256': DomainAlreadyNotPrivate,
    '261': ProcessingError,
    '262': DomainAlreadyActive,
    '263': InvalidNumberOfYears,
    '264': DomainRenewalError,
    '265': DomainTransferError,
    '266': DomainTransferDoesNotExist,
    '267': InvalidDomainName,
    '280': DNSModificationErrror,
}


class NameSilo(object):
    LIVE_BASE_URL = 'https://{live}.namesilo.com/api{batch}/'

    def __init__(self, api_key, live=False, batch=False, version='1', responseType='xml', legacy=False):
        self.api_key = api_key
        self.version = version
        self.legacy = legacy
        self.responseType = responseType
        urlDict = {'live':'sandbox', 'batch':''}
        if live: urlDict['live'] = 'www'
        if batch: urlDict['batch'] = 'batch'
        self.base_url = self.LIVE_BASE_URL.format(**urlDict)

    def __getattr__(self, name):
        if name in NAMESILO_OPERATIONS or not self.legacy:
            def handle_request(**kwargs):
                return self.request(name, **kwargs)
            return handle_request
        return super(NameSilo, self).__getattr__(name)

    def request(self, operation, **kwargs):
        if self.legacy: #Added option to use api reference or translated names
            operation = NAMESILO_OPERATIONS.get(operation, operation)

        kwargs.update(version=self.version, type=self.responseType,
                      key=self.api_key)
        r = requests.get(self.base_url + operation, params=kwargs)
        r.raise_for_status()
        response = untangle.parse(r.text)
        reply = response.namesilo.reply
        #reply = self.format_reply(reply) Removing from processing stream at this point due to issues with old xml parsing and switching to untangle
        self.handle_error(reply)
        return reply


    def handle_error(self, reply):
        code = reply.code.cdata
        if code in NAMESILO_ERRORS:
            error = NAMESILO_ERRORS[code]
            raise error(reply.detail.cdata)

    def format_reply(self, reply):
        for k, v in reply.items():
            if isinstance(v, dict):
                reply[k] = self.format_reply(v)
            elif not isinstance(v, list):
                if v.lower() == 'yes':
                    reply[k] = True
                elif v.lower() == 'no':
                    reply[k] = False
                elif v.lower() == 'n/a':
                    reply[k] = None
        return reply

