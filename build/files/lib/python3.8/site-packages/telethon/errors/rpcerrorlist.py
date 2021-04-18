from .rpcbaseerrors import RPCError, AuthKeyError, BadRequestError, FloodError, ForbiddenError, InvalidDCError, ServerError, UnauthorizedError


class TwoFaConfirmWaitError(FloodError):
    def __init__(self, request, capture=0):
        self.request = request
        self.seconds = int(capture)
        super(Exception, self).__init__('The account is 2FA protected so it will be deleted in a week. Otherwise it can be reset in {seconds}'.format(seconds=self.seconds) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.seconds)


class AboutTooLongError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided bio is too long' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AccessTokenExpiredError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Bot token expired' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AccessTokenInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided token is not valid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ActiveUserRequiredError(UnauthorizedError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The method is only available to already activated users' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AdminsTooMuchError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Too many admins' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AdminRankEmojiNotAllowedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Emoji are not allowed in admin titles or ranks' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AdminRankInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The given admin title or rank was invalid (possibly larger than 16 characters)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AlbumPhotosTooManyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Too many photos were included in the album' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ApiIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The api_id/api_hash combination is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ApiIdPublishedFloodError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("This API id was published somewhere, you can't use it now" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ArticleTitleEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The title of the article is empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AudioTitleEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The title attribute of the audio must be non-empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AuthBytesInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided authorization is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AuthKeyDuplicatedError(AuthKeyError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The authorization key (session file) was used under two different IP addresses simultaneously, and can no longer be used. Use the same session exclusively, or use different sessions' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AuthKeyInvalidError(UnauthorizedError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The key is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AuthKeyPermEmptyError(UnauthorizedError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The method is unavailable for temporary authorization key, not bound to permanent' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AuthKeyUnregisteredError(UnauthorizedError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The key is not registered in the system' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AuthRestartError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Restart the authorization process' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AuthTokenAlreadyAcceptedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The authorization token was already used' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AuthTokenExpiredError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided authorization token has expired and the updated QR-code must be re-scanned' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AuthTokenInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('An invalid authorization token was provided' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class AutoarchiveNotAvailableError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You cannot use this feature yet' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BankCardNumberInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Incorrect credit card number' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BasePortLocInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Base port location invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BannedRightsInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You cannot use that set of permissions in this request, i.e. restricting view_messages as a default' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BotsTooMuchError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('There are too many bots in this chat/channel' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BotChannelsNaError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("Bots can't edit admin privileges" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BotCommandDescriptionInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The command description was empty, too long or had invalid characters used' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BotDomainInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The domain used for the auth button does not match the one configured in @BotFather' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BotGamesDisabledError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Bot games cannot be used in this type of chat' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BotGroupsBlockedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("This bot can't be added to groups" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BotInlineDisabledError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("This bot can't be used in inline mode" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BotInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('This is not a valid bot' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BotMethodInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The API access for bot users is restricted. The method you tried to invoke cannot be executed as a bot' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BotMissingError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('This method can only be run by a bot' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BotPaymentsDisabledError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('This method can only be run by a bot' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BotPollsDisabledError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You cannot create polls under a bot account' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BotResponseTimeoutError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The bot did not answer to the callback query in time' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BroadcastCallsDisabledError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BroadcastForbiddenError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The request cannot be used in broadcast channels' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BroadcastIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The channel is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BroadcastPublicVotersForbiddenError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You cannot broadcast polls where the voters are public' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class BroadcastRequiredError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The request can only be used with a broadcast channel' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ButtonDataInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided button data is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ButtonTypeInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The type of one of the buttons you provided is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ButtonUrlInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Button URL invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class CallAlreadyAcceptedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The call was already accepted' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class CallAlreadyDeclinedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The call was already declined' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class CallOccupyFailedError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The call failed because the user is already making another call' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class CallPeerInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided call peer object is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class CallProtocolFlagsInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Call protocol flags invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class CdnMethodInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('This method cannot be invoked on a CDN server. Refer to https://core.telegram.org/cdn#schema for available methods' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChannelsAdminPublicTooMuchError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("You're admin of too many public channels, make some channels private to change the username of this channel" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChannelsTooMuchError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You have joined too many channels/supergroups' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChannelBannedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The channel is banned' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChannelInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Invalid channel object. Make sure to pass the right types, for instance making sure that the request is designed for channels or otherwise look for a different one more suited' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChannelPrivateError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The channel specified is private and you lack permission to access it. Another reason may be that you were banned from it' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChannelPublicGroupNaError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('channel/supergroup not available' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatAboutNotModifiedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('About text has not changed' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatAboutTooLongError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Chat about too long' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatAdminInviteRequiredError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You do not have the rights to do this' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatAdminRequiredError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Chat admin privileges are required to do that in the specified chat (for example, to send a message in a channel which is not yours), or invalid permissions used for the channel or group' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatForbiddenError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You cannot write in this chat' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatIdEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided chat ID is empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Invalid object ID for a chat. Make sure to pass the right types, for instance making sure that the request is designed for chats (not channels/megagroups) or otherwise look for a different one more suited\\nAn example working with a megagroup and AddChatUserRequest, it will fail because megagroups are channels. Use InviteToChannelRequest instead' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The chat is invalid for this request' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatLinkExistsError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The chat is linked to a channel and cannot be used in that request' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatNotModifiedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("The chat or channel wasn't modified (title, invites, username, admins, etc. are the same)" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatRestrictedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The chat is restricted and cannot be used in that request' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatSendGifsForbiddenError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("You can't send gifs in this chat" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatSendInlineForbiddenError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You cannot send inline results in this chat' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatSendMediaForbiddenError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("You can't send media in this chat" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatSendStickersForbiddenError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("You can't send stickers in this chat" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatTitleEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('No chat title provided' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChatWriteForbiddenError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("You can't write in this chat" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ChpCallFailError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The statistics cannot be retrieved at this time' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class CodeEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided code is empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class CodeHashInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Code hash invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class CodeInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Code invalid (i.e. from email)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ConnectionApiIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided API id is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ConnectionDeviceModelEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Device model empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ConnectionLangPackInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The specified language pack is not valid. This is meant to be used by official applications only so far, leave it empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ConnectionLayerInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The very first request must always be InvokeWithLayerRequest' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ConnectionNotInitedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Connection not initialized' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ConnectionSystemEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Connection system empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ConnectionSystemLangCodeEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The system language string was empty during connection' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ContactIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided contact ID is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ContactNameEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided contact name cannot be empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class DataInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Encrypted data invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class DataJsonInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided JSON data is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class DateEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Date empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class DcIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('This occurs when an authorization is tried to be exported for the same data center one is currently connected to' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class DhGAInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('g_a invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class DocumentInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("The document file was invalid and can't be used in inline mode" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class EmailHashExpiredError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The email hash expired and cannot be used to verify it' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class EmailInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The given email is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class EmailUnconfirmedError(BadRequestError):
    def __init__(self, request, capture=0):
        self.request = request
        self.code_length = int(capture)
        super(Exception, self).__init__('Email unconfirmed, the length of the code must be {code_length}'.format(code_length=self.code_length) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.code_length)


class EmoticonEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The emoticon field cannot be empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class EmoticonInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The specified emoticon cannot be used or was not a emoticon' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class EmoticonStickerpackMissingError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The emoticon sticker pack you are trying to get is missing' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class EncryptedMessageInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Encrypted message invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class EncryptionAlreadyAcceptedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Secret chat already accepted' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class EncryptionAlreadyDeclinedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The secret chat was already declined' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class EncryptionDeclinedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The secret chat was declined' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class EncryptionIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided secret chat ID is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class EncryptionOccupyFailedError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('TDLib developer claimed it is not an error while accepting secret chats and 500 is used instead of 420' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class EntitiesTooLongError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('It is no longer possible to send such long data inside entity tags (for example inline text URLs)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class EntityMentionUserInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("You can't use this entity" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ErrorTextEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided error message is empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ExpireForbiddenError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ExportCardInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Provided card is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ExternalUrlInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('External URL invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FieldNameEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The field with the name FIELD_NAME is missing' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FieldNameInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The field with the name FIELD_NAME is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FilerefUpgradeNeededError(AuthKeyError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The file reference needs to be refreshed before being used again' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FileIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided file id is invalid. Make sure all parameters are present, have the correct type and are not empty (ID, access hash, file reference, thumb size ...)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FileMigrateError(InvalidDCError):
    def __init__(self, request, capture=0):
        self.request = request
        self.new_dc = int(capture)
        super(Exception, self).__init__('The file to be accessed is currently stored in DC {new_dc}'.format(new_dc=self.new_dc) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.new_dc)


class FilePartsInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The number of file parts is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FilePart0MissingError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('File part 0 missing' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FilePartEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided file part is empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FilePartInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The file part number is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FilePartLengthInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The length of a file part is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FilePartSizeChangedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The file part size (chunk size) cannot change during upload' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FilePartSizeInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided file part size is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FilePartMissingError(BadRequestError):
    def __init__(self, request, capture=0):
        self.request = request
        self.which = int(capture)
        super(Exception, self).__init__('Part {which} of the file is missing from storage'.format(which=self.which) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.which)


class FileReferenceEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The file reference must exist to access the media and it cannot be empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FileReferenceExpiredError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The file reference has expired and is no longer valid or it belongs to self-destructing media and cannot be resent' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FileReferenceInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("The file reference is invalid or you can't do that operation on such message" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FirstNameInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The first name is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FloodTestPhoneWaitError(FloodError):
    def __init__(self, request, capture=0):
        self.request = request
        self.seconds = int(capture)
        super(Exception, self).__init__('A wait of {seconds} seconds is required in the test servers'.format(seconds=self.seconds) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.seconds)


class FloodWaitError(FloodError):
    def __init__(self, request, capture=0):
        self.request = request
        self.seconds = int(capture)
        super(Exception, self).__init__('A wait of {seconds} seconds is required'.format(seconds=self.seconds) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.seconds)


class FolderIdEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The folder you tried to delete was already empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FolderIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The folder you tried to use was not valid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FreshChangeAdminsForbiddenError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Recently logged-in users cannot add or change admins' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FreshChangePhoneForbiddenError(AuthKeyError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Recently logged-in users cannot use this request' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FreshResetAuthorisationForbiddenError(AuthKeyError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The current session is too new and cannot be used to reset other authorisations yet' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class FromPeerInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The given from_user peer cannot be used for the parameter' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class GameBotInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You cannot send that game with the current bot' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class GifIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided GIF ID is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class GraphOutdatedReloadError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("Data can't be used for the channel statistics, graphs outdated" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class GroupcallForbiddenError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class GroupcallSsrcDuplicateMuchError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class GroupedMediaInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Invalid grouped media' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class GroupCallInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Group call invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class HashInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided hash is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class HistoryGetFailedError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Fetching of history failed' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ImageProcessFailedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Failure while processing image' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ImportFileInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The file is too large to be imported' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ImportFormatUnrecognizedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Unknown import format' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ImportIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class InlineBotRequiredError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The action must be performed through an inline bot callback' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class InlineResultExpiredError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The inline query expired' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class InputConstructorInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided constructor is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class InputFetchErrorError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('An error occurred while deserializing TL parameters' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class InputFetchFailError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Failed deserializing TL payload' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class InputFilterInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The search query filter is valid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class InputLayerInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided layer is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class InputMethodInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The invoked method does not exist anymore or has never existed' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class InputRequestTooLongError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The input request was too long. This may be a bug in the library as it can occur when serializing more bytes than it should (like appending the vector constructor code at the end of a message)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class InputUserDeactivatedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The specified user was deleted' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class InterdcCallErrorError(ServerError):
    def __init__(self, request, capture=0):
        self.request = request
        self.dc = int(capture)
        super(Exception, self).__init__('An error occurred while communicating with DC {dc}'.format(dc=self.dc) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.dc)


class InterdcCallRichErrorError(ServerError):
    def __init__(self, request, capture=0):
        self.request = request
        self.dc = int(capture)
        super(Exception, self).__init__('A rich error occurred while communicating with DC {dc}'.format(dc=self.dc) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.dc)


class InviteHashEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The invite hash is empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class InviteHashExpiredError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The chat the user tried to join has expired and is not valid anymore' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class InviteHashInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The invite hash is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class LangPackInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided language pack is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class LastnameInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The last name is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class LimitInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('An invalid limit was provided. See https://core.telegram.org/api/files#downloading-files' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class LinkNotModifiedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The channel is already linked to this group' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class LocationInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The location given for a file was invalid. See https://core.telegram.org/api/files#downloading-files' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MaxIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided max ID is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MaxQtsInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided QTS were invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class Md5ChecksumInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The MD5 check-sums do not match' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MediaCaptionTooLongError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The caption is too long' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MediaEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided media object is invalid or the current account may not be able to send it (such as games as users)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MediaInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Media invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MediaNewInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The new media to edit the message with is invalid (such as stickers or voice notes)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MediaPrevInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The old media cannot be edited with anything else (such as stickers or voice notes)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MediaTtlInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MegagroupIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The group is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MegagroupPrehistoryHiddenError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("You can't set this discussion group because it's history is hidden" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MegagroupRequiredError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The request can only be used with a megagroup channel' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MemberNoLocationError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("An internal failure occurred while fetching user info (couldn't find location)" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MemberOccupyPrimaryLocFailedError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Occupation of primary member location failed' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MessageAuthorRequiredError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Message author required' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MessageDeleteForbiddenError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("You can't delete one of the messages you tried to delete, most likely because it is a service message." + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MessageEditTimeExpiredError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("You can't edit this message anymore, too much time has passed since its creation." + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MessageEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Empty or invalid UTF-8 message was sent' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MessageIdsEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('No message ids were provided' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MessageIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("The specified message ID is invalid or you can't do that operation on such message" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MessageNotModifiedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Content of the message was not modified' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MessagePollClosedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The poll was closed and can no longer be voted on' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MessageTooLongError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Message was too long. Current maximum length is 4096 UTF-8 characters' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MethodInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The API method is invalid and cannot be used' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MsgidDecreaseRetryError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The request should be retried with a lower message ID' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MsgIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The message ID used in the peer was invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MsgWaitFailedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('A waiting call returned an error' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MtSendQueueTooLongError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class MultiMediaTooLongError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Too many media files were included in the same album' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class NeedChatInvalidError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided chat is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class NeedMemberInvalidError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided member is invalid or does not exist (for example a thumb size)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class NetworkMigrateError(InvalidDCError):
    def __init__(self, request, capture=0):
        self.request = request
        self.new_dc = int(capture)
        super(Exception, self).__init__('The source IP address is associated with DC {new_dc}'.format(new_dc=self.new_dc) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.new_dc)


class NewSaltInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The new salt is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class NewSettingsInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The new settings are invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class NextOffsetInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The value for next_offset is invalid. Check that it has normal characters and is not too long' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class OffsetInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The given offset was invalid, it must be divisible by 1KB. See https://core.telegram.org/api/files#downloading-files' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class OffsetPeerIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided offset peer is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class OptionsTooMuchError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You defined too many options for the poll' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class OptionInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The option specified is invalid and does not exist in the target poll' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PackShortNameInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Invalid sticker pack name. It must begin with a letter, can\'t contain consecutive underscores and must end in "_by_<bot username>".' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PackShortNameOccupiedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('A stickerpack with this name already exists' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ParticipantsTooFewError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Not enough participants' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ParticipantCallFailedError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Failure while making call' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ParticipantVersionOutdatedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The other participant does not use an up to date telegram client with support for calls' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PasswordEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided password is empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PasswordHashInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The password (and thus its hash value) you entered is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PasswordMissingError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The account must have 2-factor authentication enabled (a password) before this method can be used' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PasswordRequiredError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The account must have 2-factor authentication enabled (a password) before this method can be used' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PasswordTooFreshError(BadRequestError):
    def __init__(self, request, capture=0):
        self.request = request
        self.seconds = int(capture)
        super(Exception, self).__init__('The password was added too recently and {seconds} seconds must pass before using the method'.format(seconds=self.seconds) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.seconds)


class PaymentProviderInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The payment provider was not recognised or its token was invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PeerFloodError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Too many requests' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PeerIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('An invalid Peer was used. Make sure to pass the right peer type and that the value is valid (for instance, bots cannot start conversations)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PeerIdNotSupportedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided peer ID is not supported' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PersistentTimestampEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Persistent timestamp empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PersistentTimestampInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Persistent timestamp invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PersistentTimestampOutdatedError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Persistent timestamp outdated' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhoneCodeEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The phone code is missing' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhoneCodeExpiredError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The confirmation code has expired' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhoneCodeHashEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The phone code hash is missing' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhoneCodeInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The phone code entered was invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhoneMigrateError(InvalidDCError):
    def __init__(self, request, capture=0):
        self.request = request
        self.new_dc = int(capture)
        super(Exception, self).__init__('The phone number a user is trying to use for authorization is associated with DC {new_dc}'.format(new_dc=self.new_dc) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.new_dc)


class PhoneNumberAppSignupForbiddenError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("You can't sign up using this app" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhoneNumberBannedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The used phone number has been banned from Telegram and cannot be used anymore. Maybe check https://www.telegram.org/faq_spam' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhoneNumberFloodError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You asked for the code too many times.' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhoneNumberInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The phone number is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhoneNumberOccupiedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The phone number is already in use' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhoneNumberUnoccupiedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The phone number is not yet being used' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhonePasswordFloodError(AuthKeyError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You have tried logging in too many times' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhonePasswordProtectedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('This phone is password protected' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhotoContentUrlEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The content from the URL used as a photo appears to be empty or has caused another HTTP error' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhotoCropSizeSmallError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Photo is too small' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhotoExtInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The extension of the photo is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhotoIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Photo id is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhotoInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Photo invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhotoInvalidDimensionsError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The photo dimensions are invalid (hint: `pip install pillow` for `send_file` to resize images)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhotoSaveFileInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The photo you tried to send cannot be saved by Telegram. A reason may be that it exceeds 10MB. Try resizing it locally' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PhotoThumbUrlEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The URL used as a thumbnail appears to be empty or has caused another HTTP error' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PinRestrictedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("You can't pin messages in private chats with other people" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PollAnswersInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The poll did not have enough answers or had too many' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PollOptionDuplicateError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('A duplicate option was sent in the same poll' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PollOptionInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('A poll option used invalid data (the data may be too long)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PollQuestionInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The poll question was either empty or too long' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PollUnsupportedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('This layer does not support polls in the issued method' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PreviousChatImportActiveWaitMinError(AuthKeyError):
    def __init__(self, request, capture=0):
        self.request = request
        self.minutes = int(capture)
        super(Exception, self).__init__('Similar to a flood wait, must wait {minutes} minutes'.format(minutes=self.minutes) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.minutes)


class PrivacyKeyInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The privacy key is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PrivacyTooLongError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Cannot add that many entities in a single request' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PrivacyValueInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The privacy value is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class PtsChangeEmptyError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('No PTS change' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class QueryIdEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The query ID is empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class QueryIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The query ID is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class QueryTooShortError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The query string is too short' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class QuizCorrectAnswersEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('A quiz must specify one correct answer' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class QuizCorrectAnswersTooMuchError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('There can only be one correct answer' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class QuizCorrectAnswerInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The correct answer is not an existing answer' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class QuizMultipleInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('A poll cannot be both multiple choice and quiz' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class RandomIdDuplicateError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You provided a random ID that was already used' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class RandomIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('A provided random ID is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class RandomLengthInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Random length invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class RangesInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Invalid range provided' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ReactionEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('No reaction provided' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ReactionInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Invalid reaction provided (only emoji are allowed)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ReflectorNotAvailableError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Invalid call reflector server' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class RegIdGenerateFailedError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Failure while generating registration ID' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ReplyMarkupGameEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided reply markup for the game is empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ReplyMarkupInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided reply markup is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ReplyMarkupTooLongError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The data embedded in the reply markup buttons was too much' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ResultsTooMuchError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You sent too many results, see https://core.telegram.org/bots/api#answerinlinequery for the current limit' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ResultIdDuplicateError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Duplicated IDs on the sent results. Make sure to use unique IDs' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ResultIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The given result cannot be used to send the selection to the bot' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ResultTypeInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Result type invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class RightForbiddenError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Either your admin rights do not allow you to do this or you passed the wrong rights combination (some rights only apply to channels and vice versa)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class RpcCallFailError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Telegram is having internal issues, please try again later.' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class RpcMcgetFailError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Telegram is having internal issues, please try again later.' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class RsaDecryptFailedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Internal RSA decryption failed' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ScheduleBotNotAllowedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Bots are not allowed to schedule messages' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ScheduleDateTooLateError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The date you tried to schedule is too far in the future (last known limit of 1 year and a few hours)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ScheduleStatusPrivateError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You cannot schedule a message until the person comes online if their privacy does not show this information' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ScheduleTooMuchError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You cannot schedule more messages in this chat (last known limit of 100 per chat)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class SearchQueryEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The search query is empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class SecondsInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Slow mode only supports certain values (e.g. 0, 10s, 30s, 1m, 5m, 15m and 1h)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class SendMessageMediaInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The message media was invalid or not specified' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class SendMessageTypeInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The message type is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class SensitiveChangeForbiddenError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Your sensitive content settings cannot be changed at this time' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class SessionExpiredError(UnauthorizedError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The authorization has expired' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class SessionPasswordNeededError(UnauthorizedError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Two-steps verification is enabled and a password is required' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class SessionRevokedError(UnauthorizedError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The authorization has been invalidated, because of the user terminating all sessions' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class SessionTooFreshError(BadRequestError):
    def __init__(self, request, capture=0):
        self.request = request
        self.seconds = int(capture)
        super(Exception, self).__init__('The session logged in too recently and {seconds} seconds must pass before calling the method'.format(seconds=self.seconds) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.seconds)


class Sha256HashInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided SHA256 hash is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ShortnameOccupyFailedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('An error occurred when trying to register the short-name used for the sticker pack. Try a different name' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class SlowModeWaitError(FloodError):
    def __init__(self, request, capture=0):
        self.request = request
        self.seconds = int(capture)
        super(Exception, self).__init__('A wait of {seconds} seconds is required before sending another message in this chat'.format(seconds=self.seconds) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.seconds)


class SrpIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class StartParamEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The start parameter is empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class StartParamInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Start parameter invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class StatsMigrateError(InvalidDCError):
    def __init__(self, request, capture=0):
        self.request = request
        self.dc = int(capture)
        super(Exception, self).__init__('The channel statistics must be fetched from DC {dc}'.format(dc=self.dc) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.dc)


class StickersetInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided sticker set is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class StickersetOwnerAnonymousError(AuthKeyError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("This sticker set can't be used as the group's official stickers because it was created by one of its anonymous admins" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class StickersEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('No sticker provided' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class StickerDocumentInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The sticker file was invalid (this file has failed Telegram internal checks, make sure to use the correct format and comply with https://core.telegram.org/animated_stickers)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class StickerEmojiInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Sticker emoji invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class StickerFileInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Sticker file invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class StickerIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided sticker ID is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class StickerInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided sticker is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class StickerPngDimensionsError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Sticker png dimensions invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class StickerPngNopngError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Stickers must be a png file but the used image was not a png' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class StorageCheckFailedError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Server storage check failed' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class StoreInvalidScalarTypeError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class TakeoutInitDelayError(FloodError):
    def __init__(self, request, capture=0):
        self.request = request
        self.seconds = int(capture)
        super(Exception, self).__init__('A wait of {seconds} seconds is required before being able to initiate the takeout'.format(seconds=self.seconds) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.seconds)


class TakeoutInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The takeout session has been invalidated by another data export session' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class TakeoutRequiredError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You must initialize a takeout request first' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class TempAuthKeyEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('No temporary auth key provided' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class TimeoutError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('A timeout occurred while fetching data from the worker' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ThemeInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Theme invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class ThemeMimeInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You cannot create this theme, the mime-type is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class TmpPasswordDisabledError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The temporary password is disabled' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class TokenInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided token is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class TtlDaysInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided TTL is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class TypesEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The types field is empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class TypeConstructorInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The type constructor is invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UnknownMethodError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The method you tried to call cannot be called on non-CDN DCs' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UntilDateInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('That date cannot be specified in this request (try using None)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UrlInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("The URL used was invalid (e.g. when answering a callback with a URL that's not t.me/yourbot or your game's URL)" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UsernameInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Nobody is using this username, or the username is unacceptable. If the latter, it must match r"[a-zA-Z][\\w\\d]{3,30}[a-zA-Z\\d]"' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UsernameNotModifiedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The username is not different from the current username' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UsernameNotOccupiedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The username is not in use by anyone else yet' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UsernameOccupiedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The username is already taken' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UsersTooFewError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Not enough users (to create a chat, for example)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UsersTooMuchError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The maximum number of users has been exceeded (to create a chat, for example)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserAdminInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("Either you're not an admin or you tried to ban an admin that you didn't promote" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserAlreadyParticipantError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The authenticated user is already a participant of the chat' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserBannedInChannelError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("You're banned from sending messages in supergroups/channels" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserBlockedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('User blocked' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserBotError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Bots can only be admins in channels.' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserBotInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('This method can only be called by a bot' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserBotRequiredError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('This method can only be called by a bot' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserChannelsTooMuchError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('One of the users you tried to add is already in too many channels/supergroups' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserCreatorError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("You can't leave this channel, because you're its creator" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserDeactivatedError(UnauthorizedError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The user has been deleted/deactivated' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserDeactivatedBanError(UnauthorizedError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The user has been deleted/deactivated' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserIdInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Invalid object ID for a user. Make sure to pass the right types, for instance making sure that the request is designed for users or otherwise look for a different one more suited' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The given user was invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserIsBlockedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('User is blocked' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserIsBotError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("Bots can't send messages to other bots" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserKickedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('This user was kicked from this supergroup/channel' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserMigrateError(InvalidDCError):
    def __init__(self, request, capture=0):
        self.request = request
        self.new_dc = int(capture)
        super(Exception, self).__init__('The user whose identity is being used to execute queries is associated with DC {new_dc}'.format(new_dc=self.new_dc) + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request, self.new_dc)


class UserNotMutualContactError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The provided user is not a mutual contact' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserNotParticipantError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The target user is not a member of the specified megagroup or channel' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserPrivacyRestrictedError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("The user's privacy settings do not allow you to do this" + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class UserRestrictedError(ForbiddenError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__("You're spamreported, you can't create channels or chats." + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class VideoContentTypeInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The video content type is not supported with the given parameters (i.e. supports_streaming)' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class VideoFileInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The given video cannot be used' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class WallpaperFileInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The given file cannot be used as a wallpaper' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class WallpaperInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The input wallpaper was not valid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class WcConvertUrlInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('WC convert URL invalid' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class WebdocumentUrlInvalidError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('The given URL cannot be used' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class WebpageCurlFailedError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Failure while fetching the webpage with cURL' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class WebpageMediaEmptyError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Webpage media empty' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class WorkerBusyTooLongRetryError(ServerError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('Telegram workers are too busy to respond immediately' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


class YouBlockedUserError(BadRequestError):
    def __init__(self, request):
        self.request = request
        super(Exception, self).__init__('You blocked this user' + self._fmt_request(self.request))

    def __reduce__(self):
        return type(self), (self.request,)


rpc_errors_dict = {
    'ABOUT_TOO_LONG': AboutTooLongError,
    'ACCESS_TOKEN_EXPIRED': AccessTokenExpiredError,
    'ACCESS_TOKEN_INVALID': AccessTokenInvalidError,
    'ACTIVE_USER_REQUIRED': ActiveUserRequiredError,
    'ADMINS_TOO_MUCH': AdminsTooMuchError,
    'ADMIN_RANK_EMOJI_NOT_ALLOWED': AdminRankEmojiNotAllowedError,
    'ADMIN_RANK_INVALID': AdminRankInvalidError,
    'ALBUM_PHOTOS_TOO_MANY': AlbumPhotosTooManyError,
    'API_ID_INVALID': ApiIdInvalidError,
    'API_ID_PUBLISHED_FLOOD': ApiIdPublishedFloodError,
    'ARTICLE_TITLE_EMPTY': ArticleTitleEmptyError,
    'AUDIO_TITLE_EMPTY': AudioTitleEmptyError,
    'AUTH_BYTES_INVALID': AuthBytesInvalidError,
    'AUTH_KEY_DUPLICATED': AuthKeyDuplicatedError,
    'AUTH_KEY_INVALID': AuthKeyInvalidError,
    'AUTH_KEY_PERM_EMPTY': AuthKeyPermEmptyError,
    'AUTH_KEY_UNREGISTERED': AuthKeyUnregisteredError,
    'AUTH_RESTART': AuthRestartError,
    'AUTH_TOKEN_ALREADY_ACCEPTED': AuthTokenAlreadyAcceptedError,
    'AUTH_TOKEN_EXPIRED': AuthTokenExpiredError,
    'AUTH_TOKEN_INVALID': AuthTokenInvalidError,
    'AUTOARCHIVE_NOT_AVAILABLE': AutoarchiveNotAvailableError,
    'BANK_CARD_NUMBER_INVALID': BankCardNumberInvalidError,
    'BASE_PORT_LOC_INVALID': BasePortLocInvalidError,
    'BANNED_RIGHTS_INVALID': BannedRightsInvalidError,
    'BOTS_TOO_MUCH': BotsTooMuchError,
    'BOT_CHANNELS_NA': BotChannelsNaError,
    'BOT_COMMAND_DESCRIPTION_INVALID': BotCommandDescriptionInvalidError,
    'BOT_DOMAIN_INVALID': BotDomainInvalidError,
    'BOT_GAMES_DISABLED': BotGamesDisabledError,
    'BOT_GROUPS_BLOCKED': BotGroupsBlockedError,
    'BOT_INLINE_DISABLED': BotInlineDisabledError,
    'BOT_INVALID': BotInvalidError,
    'BOT_METHOD_INVALID': BotMethodInvalidError,
    'BOT_MISSING': BotMissingError,
    'BOT_PAYMENTS_DISABLED': BotPaymentsDisabledError,
    'BOT_POLLS_DISABLED': BotPollsDisabledError,
    'BOT_RESPONSE_TIMEOUT': BotResponseTimeoutError,
    'BROADCAST_CALLS_DISABLED': BroadcastCallsDisabledError,
    'BROADCAST_FORBIDDEN': BroadcastForbiddenError,
    'BROADCAST_ID_INVALID': BroadcastIdInvalidError,
    'BROADCAST_PUBLIC_VOTERS_FORBIDDEN': BroadcastPublicVotersForbiddenError,
    'BROADCAST_REQUIRED': BroadcastRequiredError,
    'BUTTON_DATA_INVALID': ButtonDataInvalidError,
    'BUTTON_TYPE_INVALID': ButtonTypeInvalidError,
    'BUTTON_URL_INVALID': ButtonUrlInvalidError,
    'CALL_ALREADY_ACCEPTED': CallAlreadyAcceptedError,
    'CALL_ALREADY_DECLINED': CallAlreadyDeclinedError,
    'CALL_OCCUPY_FAILED': CallOccupyFailedError,
    'CALL_PEER_INVALID': CallPeerInvalidError,
    'CALL_PROTOCOL_FLAGS_INVALID': CallProtocolFlagsInvalidError,
    'CDN_METHOD_INVALID': CdnMethodInvalidError,
    'CHANNELS_ADMIN_PUBLIC_TOO_MUCH': ChannelsAdminPublicTooMuchError,
    'CHANNELS_TOO_MUCH': ChannelsTooMuchError,
    'CHANNEL_BANNED': ChannelBannedError,
    'CHANNEL_INVALID': ChannelInvalidError,
    'CHANNEL_PRIVATE': ChannelPrivateError,
    'CHANNEL_PUBLIC_GROUP_NA': ChannelPublicGroupNaError,
    'CHAT_ABOUT_NOT_MODIFIED': ChatAboutNotModifiedError,
    'CHAT_ABOUT_TOO_LONG': ChatAboutTooLongError,
    'CHAT_ADMIN_INVITE_REQUIRED': ChatAdminInviteRequiredError,
    'CHAT_ADMIN_REQUIRED': ChatAdminRequiredError,
    'CHAT_FORBIDDEN': ChatForbiddenError,
    'CHAT_ID_EMPTY': ChatIdEmptyError,
    'CHAT_ID_INVALID': ChatIdInvalidError,
    'CHAT_INVALID': ChatInvalidError,
    'CHAT_LINK_EXISTS': ChatLinkExistsError,
    'CHAT_NOT_MODIFIED': ChatNotModifiedError,
    'CHAT_RESTRICTED': ChatRestrictedError,
    'CHAT_SEND_GIFS_FORBIDDEN': ChatSendGifsForbiddenError,
    'CHAT_SEND_INLINE_FORBIDDEN': ChatSendInlineForbiddenError,
    'CHAT_SEND_MEDIA_FORBIDDEN': ChatSendMediaForbiddenError,
    'CHAT_SEND_STICKERS_FORBIDDEN': ChatSendStickersForbiddenError,
    'CHAT_TITLE_EMPTY': ChatTitleEmptyError,
    'CHAT_WRITE_FORBIDDEN': ChatWriteForbiddenError,
    'CHP_CALL_FAIL': ChpCallFailError,
    'CODE_EMPTY': CodeEmptyError,
    'CODE_HASH_INVALID': CodeHashInvalidError,
    'CODE_INVALID': CodeInvalidError,
    'CONNECTION_API_ID_INVALID': ConnectionApiIdInvalidError,
    'CONNECTION_DEVICE_MODEL_EMPTY': ConnectionDeviceModelEmptyError,
    'CONNECTION_LANG_PACK_INVALID': ConnectionLangPackInvalidError,
    'CONNECTION_LAYER_INVALID': ConnectionLayerInvalidError,
    'CONNECTION_NOT_INITED': ConnectionNotInitedError,
    'CONNECTION_SYSTEM_EMPTY': ConnectionSystemEmptyError,
    'CONNECTION_SYSTEM_LANG_CODE_EMPTY': ConnectionSystemLangCodeEmptyError,
    'CONTACT_ID_INVALID': ContactIdInvalidError,
    'CONTACT_NAME_EMPTY': ContactNameEmptyError,
    'DATA_INVALID': DataInvalidError,
    'DATA_JSON_INVALID': DataJsonInvalidError,
    'DATE_EMPTY': DateEmptyError,
    'DC_ID_INVALID': DcIdInvalidError,
    'DH_G_A_INVALID': DhGAInvalidError,
    'DOCUMENT_INVALID': DocumentInvalidError,
    'EMAIL_HASH_EXPIRED': EmailHashExpiredError,
    'EMAIL_INVALID': EmailInvalidError,
    'EMOTICON_EMPTY': EmoticonEmptyError,
    'EMOTICON_INVALID': EmoticonInvalidError,
    'EMOTICON_STICKERPACK_MISSING': EmoticonStickerpackMissingError,
    'ENCRYPTED_MESSAGE_INVALID': EncryptedMessageInvalidError,
    'ENCRYPTION_ALREADY_ACCEPTED': EncryptionAlreadyAcceptedError,
    'ENCRYPTION_ALREADY_DECLINED': EncryptionAlreadyDeclinedError,
    'ENCRYPTION_DECLINED': EncryptionDeclinedError,
    'ENCRYPTION_ID_INVALID': EncryptionIdInvalidError,
    'ENCRYPTION_OCCUPY_FAILED': EncryptionOccupyFailedError,
    'ENTITIES_TOO_LONG': EntitiesTooLongError,
    'ENTITY_MENTION_USER_INVALID': EntityMentionUserInvalidError,
    'ERROR_TEXT_EMPTY': ErrorTextEmptyError,
    'EXPIRE_FORBIDDEN': ExpireForbiddenError,
    'EXPORT_CARD_INVALID': ExportCardInvalidError,
    'EXTERNAL_URL_INVALID': ExternalUrlInvalidError,
    'FIELD_NAME_EMPTY': FieldNameEmptyError,
    'FIELD_NAME_INVALID': FieldNameInvalidError,
    'FILEREF_UPGRADE_NEEDED': FilerefUpgradeNeededError,
    'FILE_ID_INVALID': FileIdInvalidError,
    'FILE_PARTS_INVALID': FilePartsInvalidError,
    'FILE_PART_0_MISSING': FilePart0MissingError,
    'FILE_PART_EMPTY': FilePartEmptyError,
    'FILE_PART_INVALID': FilePartInvalidError,
    'FILE_PART_LENGTH_INVALID': FilePartLengthInvalidError,
    'FILE_PART_SIZE_CHANGED': FilePartSizeChangedError,
    'FILE_PART_SIZE_INVALID': FilePartSizeInvalidError,
    'FILE_REFERENCE_EMPTY': FileReferenceEmptyError,
    'FILE_REFERENCE_EXPIRED': FileReferenceExpiredError,
    'FILE_REFERENCE_INVALID': FileReferenceInvalidError,
    'FIRSTNAME_INVALID': FirstNameInvalidError,
    'FOLDER_ID_EMPTY': FolderIdEmptyError,
    'FOLDER_ID_INVALID': FolderIdInvalidError,
    'FRESH_CHANGE_ADMINS_FORBIDDEN': FreshChangeAdminsForbiddenError,
    'FRESH_CHANGE_PHONE_FORBIDDEN': FreshChangePhoneForbiddenError,
    'FRESH_RESET_AUTHORISATION_FORBIDDEN': FreshResetAuthorisationForbiddenError,
    'FROM_PEER_INVALID': FromPeerInvalidError,
    'GAME_BOT_INVALID': GameBotInvalidError,
    'GIF_ID_INVALID': GifIdInvalidError,
    'GRAPH_OUTDATED_RELOAD': GraphOutdatedReloadError,
    'GROUPCALL_FORBIDDEN': GroupcallForbiddenError,
    'GROUPCALL_SSRC_DUPLICATE_MUCH': GroupcallSsrcDuplicateMuchError,
    'GROUPED_MEDIA_INVALID': GroupedMediaInvalidError,
    'GROUP_CALL_INVALID': GroupCallInvalidError,
    'HASH_INVALID': HashInvalidError,
    'HISTORY_GET_FAILED': HistoryGetFailedError,
    'IMAGE_PROCESS_FAILED': ImageProcessFailedError,
    'IMPORT_FILE_INVALID': ImportFileInvalidError,
    'IMPORT_FORMAT_UNRECOGNIZED': ImportFormatUnrecognizedError,
    'IMPORT_ID_INVALID': ImportIdInvalidError,
    'INLINE_BOT_REQUIRED': InlineBotRequiredError,
    'INLINE_RESULT_EXPIRED': InlineResultExpiredError,
    'INPUT_CONSTRUCTOR_INVALID': InputConstructorInvalidError,
    'INPUT_FETCH_ERROR': InputFetchErrorError,
    'INPUT_FETCH_FAIL': InputFetchFailError,
    'INPUT_FILTER_INVALID': InputFilterInvalidError,
    'INPUT_LAYER_INVALID': InputLayerInvalidError,
    'INPUT_METHOD_INVALID': InputMethodInvalidError,
    'INPUT_REQUEST_TOO_LONG': InputRequestTooLongError,
    'INPUT_USER_DEACTIVATED': InputUserDeactivatedError,
    'INVITE_HASH_EMPTY': InviteHashEmptyError,
    'INVITE_HASH_EXPIRED': InviteHashExpiredError,
    'INVITE_HASH_INVALID': InviteHashInvalidError,
    'LANG_PACK_INVALID': LangPackInvalidError,
    'LASTNAME_INVALID': LastnameInvalidError,
    'LIMIT_INVALID': LimitInvalidError,
    'LINK_NOT_MODIFIED': LinkNotModifiedError,
    'LOCATION_INVALID': LocationInvalidError,
    'MAX_ID_INVALID': MaxIdInvalidError,
    'MAX_QTS_INVALID': MaxQtsInvalidError,
    'MD5_CHECKSUM_INVALID': Md5ChecksumInvalidError,
    'MEDIA_CAPTION_TOO_LONG': MediaCaptionTooLongError,
    'MEDIA_EMPTY': MediaEmptyError,
    'MEDIA_INVALID': MediaInvalidError,
    'MEDIA_NEW_INVALID': MediaNewInvalidError,
    'MEDIA_PREV_INVALID': MediaPrevInvalidError,
    'MEDIA_TTL_INVALID': MediaTtlInvalidError,
    'MEGAGROUP_ID_INVALID': MegagroupIdInvalidError,
    'MEGAGROUP_PREHISTORY_HIDDEN': MegagroupPrehistoryHiddenError,
    'MEGAGROUP_REQUIRED': MegagroupRequiredError,
    'MEMBER_NO_LOCATION': MemberNoLocationError,
    'MEMBER_OCCUPY_PRIMARY_LOC_FAILED': MemberOccupyPrimaryLocFailedError,
    'MESSAGE_AUTHOR_REQUIRED': MessageAuthorRequiredError,
    'MESSAGE_DELETE_FORBIDDEN': MessageDeleteForbiddenError,
    'MESSAGE_EDIT_TIME_EXPIRED': MessageEditTimeExpiredError,
    'MESSAGE_EMPTY': MessageEmptyError,
    'MESSAGE_IDS_EMPTY': MessageIdsEmptyError,
    'MESSAGE_ID_INVALID': MessageIdInvalidError,
    'MESSAGE_NOT_MODIFIED': MessageNotModifiedError,
    'MESSAGE_POLL_CLOSED': MessagePollClosedError,
    'MESSAGE_TOO_LONG': MessageTooLongError,
    'METHOD_INVALID': MethodInvalidError,
    'MSGID_DECREASE_RETRY': MsgidDecreaseRetryError,
    'MSG_ID_INVALID': MsgIdInvalidError,
    'MSG_WAIT_FAILED': MsgWaitFailedError,
    'MT_SEND_QUEUE_TOO_LONG': MtSendQueueTooLongError,
    'MULTI_MEDIA_TOO_LONG': MultiMediaTooLongError,
    'NEED_CHAT_INVALID': NeedChatInvalidError,
    'NEED_MEMBER_INVALID': NeedMemberInvalidError,
    'NEW_SALT_INVALID': NewSaltInvalidError,
    'NEW_SETTINGS_INVALID': NewSettingsInvalidError,
    'NEXT_OFFSET_INVALID': NextOffsetInvalidError,
    'OFFSET_INVALID': OffsetInvalidError,
    'OFFSET_PEER_ID_INVALID': OffsetPeerIdInvalidError,
    'OPTIONS_TOO_MUCH': OptionsTooMuchError,
    'OPTION_INVALID': OptionInvalidError,
    'PACK_SHORT_NAME_INVALID': PackShortNameInvalidError,
    'PACK_SHORT_NAME_OCCUPIED': PackShortNameOccupiedError,
    'PARTICIPANTS_TOO_FEW': ParticipantsTooFewError,
    'PARTICIPANT_CALL_FAILED': ParticipantCallFailedError,
    'PARTICIPANT_VERSION_OUTDATED': ParticipantVersionOutdatedError,
    'PASSWORD_EMPTY': PasswordEmptyError,
    'PASSWORD_HASH_INVALID': PasswordHashInvalidError,
    'PASSWORD_MISSING': PasswordMissingError,
    'PASSWORD_REQUIRED': PasswordRequiredError,
    'PAYMENT_PROVIDER_INVALID': PaymentProviderInvalidError,
    'PEER_FLOOD': PeerFloodError,
    'PEER_ID_INVALID': PeerIdInvalidError,
    'PEER_ID_NOT_SUPPORTED': PeerIdNotSupportedError,
    'PERSISTENT_TIMESTAMP_EMPTY': PersistentTimestampEmptyError,
    'PERSISTENT_TIMESTAMP_INVALID': PersistentTimestampInvalidError,
    'PERSISTENT_TIMESTAMP_OUTDATED': PersistentTimestampOutdatedError,
    'PHONE_CODE_EMPTY': PhoneCodeEmptyError,
    'PHONE_CODE_EXPIRED': PhoneCodeExpiredError,
    'PHONE_CODE_HASH_EMPTY': PhoneCodeHashEmptyError,
    'PHONE_CODE_INVALID': PhoneCodeInvalidError,
    'PHONE_NUMBER_APP_SIGNUP_FORBIDDEN': PhoneNumberAppSignupForbiddenError,
    'PHONE_NUMBER_BANNED': PhoneNumberBannedError,
    'PHONE_NUMBER_FLOOD': PhoneNumberFloodError,
    'PHONE_NUMBER_INVALID': PhoneNumberInvalidError,
    'PHONE_NUMBER_OCCUPIED': PhoneNumberOccupiedError,
    'PHONE_NUMBER_UNOCCUPIED': PhoneNumberUnoccupiedError,
    'PHONE_PASSWORD_FLOOD': PhonePasswordFloodError,
    'PHONE_PASSWORD_PROTECTED': PhonePasswordProtectedError,
    'PHOTO_CONTENT_URL_EMPTY': PhotoContentUrlEmptyError,
    'PHOTO_CROP_SIZE_SMALL': PhotoCropSizeSmallError,
    'PHOTO_EXT_INVALID': PhotoExtInvalidError,
    'PHOTO_ID_INVALID': PhotoIdInvalidError,
    'PHOTO_INVALID': PhotoInvalidError,
    'PHOTO_INVALID_DIMENSIONS': PhotoInvalidDimensionsError,
    'PHOTO_SAVE_FILE_INVALID': PhotoSaveFileInvalidError,
    'PHOTO_THUMB_URL_EMPTY': PhotoThumbUrlEmptyError,
    'PIN_RESTRICTED': PinRestrictedError,
    'POLL_ANSWERS_INVALID': PollAnswersInvalidError,
    'POLL_OPTION_DUPLICATE': PollOptionDuplicateError,
    'POLL_OPTION_INVALID': PollOptionInvalidError,
    'POLL_QUESTION_INVALID': PollQuestionInvalidError,
    'POLL_UNSUPPORTED': PollUnsupportedError,
    'PRIVACY_KEY_INVALID': PrivacyKeyInvalidError,
    'PRIVACY_TOO_LONG': PrivacyTooLongError,
    'PRIVACY_VALUE_INVALID': PrivacyValueInvalidError,
    'PTS_CHANGE_EMPTY': PtsChangeEmptyError,
    'QUERY_ID_EMPTY': QueryIdEmptyError,
    'QUERY_ID_INVALID': QueryIdInvalidError,
    'QUERY_TOO_SHORT': QueryTooShortError,
    'QUIZ_CORRECT_ANSWERS_EMPTY': QuizCorrectAnswersEmptyError,
    'QUIZ_CORRECT_ANSWERS_TOO_MUCH': QuizCorrectAnswersTooMuchError,
    'QUIZ_CORRECT_ANSWER_INVALID': QuizCorrectAnswerInvalidError,
    'QUIZ_MULTIPLE_INVALID': QuizMultipleInvalidError,
    'RANDOM_ID_DUPLICATE': RandomIdDuplicateError,
    'RANDOM_ID_INVALID': RandomIdInvalidError,
    'RANDOM_LENGTH_INVALID': RandomLengthInvalidError,
    'RANGES_INVALID': RangesInvalidError,
    'REACTION_EMPTY': ReactionEmptyError,
    'REACTION_INVALID': ReactionInvalidError,
    'REFLECTOR_NOT_AVAILABLE': ReflectorNotAvailableError,
    'REG_ID_GENERATE_FAILED': RegIdGenerateFailedError,
    'REPLY_MARKUP_GAME_EMPTY': ReplyMarkupGameEmptyError,
    'REPLY_MARKUP_INVALID': ReplyMarkupInvalidError,
    'REPLY_MARKUP_TOO_LONG': ReplyMarkupTooLongError,
    'RESULTS_TOO_MUCH': ResultsTooMuchError,
    'RESULT_ID_DUPLICATE': ResultIdDuplicateError,
    'RESULT_ID_INVALID': ResultIdInvalidError,
    'RESULT_TYPE_INVALID': ResultTypeInvalidError,
    'RIGHT_FORBIDDEN': RightForbiddenError,
    'RPC_CALL_FAIL': RpcCallFailError,
    'RPC_MCGET_FAIL': RpcMcgetFailError,
    'RSA_DECRYPT_FAILED': RsaDecryptFailedError,
    'SCHEDULE_BOT_NOT_ALLOWED': ScheduleBotNotAllowedError,
    'SCHEDULE_DATE_TOO_LATE': ScheduleDateTooLateError,
    'SCHEDULE_STATUS_PRIVATE': ScheduleStatusPrivateError,
    'SCHEDULE_TOO_MUCH': ScheduleTooMuchError,
    'SEARCH_QUERY_EMPTY': SearchQueryEmptyError,
    'SECONDS_INVALID': SecondsInvalidError,
    'SEND_MESSAGE_MEDIA_INVALID': SendMessageMediaInvalidError,
    'SEND_MESSAGE_TYPE_INVALID': SendMessageTypeInvalidError,
    'SENSITIVE_CHANGE_FORBIDDEN': SensitiveChangeForbiddenError,
    'SESSION_EXPIRED': SessionExpiredError,
    'SESSION_PASSWORD_NEEDED': SessionPasswordNeededError,
    'SESSION_REVOKED': SessionRevokedError,
    'SHA256_HASH_INVALID': Sha256HashInvalidError,
    'SHORTNAME_OCCUPY_FAILED': ShortnameOccupyFailedError,
    'SRP_ID_INVALID': SrpIdInvalidError,
    'START_PARAM_EMPTY': StartParamEmptyError,
    'START_PARAM_INVALID': StartParamInvalidError,
    'STICKERSET_INVALID': StickersetInvalidError,
    'STICKERSET_OWNER_ANONYMOUS': StickersetOwnerAnonymousError,
    'STICKERS_EMPTY': StickersEmptyError,
    'STICKER_DOCUMENT_INVALID': StickerDocumentInvalidError,
    'STICKER_EMOJI_INVALID': StickerEmojiInvalidError,
    'STICKER_FILE_INVALID': StickerFileInvalidError,
    'STICKER_ID_INVALID': StickerIdInvalidError,
    'STICKER_INVALID': StickerInvalidError,
    'STICKER_PNG_DIMENSIONS': StickerPngDimensionsError,
    'STICKER_PNG_NOPNG': StickerPngNopngError,
    'STORAGE_CHECK_FAILED': StorageCheckFailedError,
    'STORE_INVALID_SCALAR_TYPE': StoreInvalidScalarTypeError,
    'TAKEOUT_INVALID': TakeoutInvalidError,
    'TAKEOUT_REQUIRED': TakeoutRequiredError,
    'TEMP_AUTH_KEY_EMPTY': TempAuthKeyEmptyError,
    'TIMEOUT': TimeoutError,
    'THEME_INVALID': ThemeInvalidError,
    'THEME_MIME_INVALID': ThemeMimeInvalidError,
    'TMP_PASSWORD_DISABLED': TmpPasswordDisabledError,
    'TOKEN_INVALID': TokenInvalidError,
    'TTL_DAYS_INVALID': TtlDaysInvalidError,
    'TYPES_EMPTY': TypesEmptyError,
    'TYPE_CONSTRUCTOR_INVALID': TypeConstructorInvalidError,
    'UNKNOWN_METHOD': UnknownMethodError,
    'UNTIL_DATE_INVALID': UntilDateInvalidError,
    'URL_INVALID': UrlInvalidError,
    'USERNAME_INVALID': UsernameInvalidError,
    'USERNAME_NOT_MODIFIED': UsernameNotModifiedError,
    'USERNAME_NOT_OCCUPIED': UsernameNotOccupiedError,
    'USERNAME_OCCUPIED': UsernameOccupiedError,
    'USERS_TOO_FEW': UsersTooFewError,
    'USERS_TOO_MUCH': UsersTooMuchError,
    'USER_ADMIN_INVALID': UserAdminInvalidError,
    'USER_ALREADY_PARTICIPANT': UserAlreadyParticipantError,
    'USER_BANNED_IN_CHANNEL': UserBannedInChannelError,
    'USER_BLOCKED': UserBlockedError,
    'USER_BOT': UserBotError,
    'USER_BOT_INVALID': UserBotInvalidError,
    'USER_BOT_REQUIRED': UserBotRequiredError,
    'USER_CHANNELS_TOO_MUCH': UserChannelsTooMuchError,
    'USER_CREATOR': UserCreatorError,
    'USER_DEACTIVATED': UserDeactivatedError,
    'USER_DEACTIVATED_BAN': UserDeactivatedBanError,
    'USER_ID_INVALID': UserIdInvalidError,
    'USER_INVALID': UserInvalidError,
    'USER_IS_BLOCKED': UserIsBlockedError,
    'USER_IS_BOT': UserIsBotError,
    'USER_KICKED': UserKickedError,
    'USER_NOT_MUTUAL_CONTACT': UserNotMutualContactError,
    'USER_NOT_PARTICIPANT': UserNotParticipantError,
    'USER_PRIVACY_RESTRICTED': UserPrivacyRestrictedError,
    'USER_RESTRICTED': UserRestrictedError,
    'VIDEO_CONTENT_TYPE_INVALID': VideoContentTypeInvalidError,
    'VIDEO_FILE_INVALID': VideoFileInvalidError,
    'WALLPAPER_FILE_INVALID': WallpaperFileInvalidError,
    'WALLPAPER_INVALID': WallpaperInvalidError,
    'WC_CONVERT_URL_INVALID': WcConvertUrlInvalidError,
    'WEBDOCUMENT_URL_INVALID': WebdocumentUrlInvalidError,
    'WEBPAGE_CURL_FAILED': WebpageCurlFailedError,
    'WEBPAGE_MEDIA_EMPTY': WebpageMediaEmptyError,
    'WORKER_BUSY_TOO_LONG_RETRY': WorkerBusyTooLongRetryError,
    'YOU_BLOCKED_USER': YouBlockedUserError,
}

rpc_errors_re = (
    ('2FA_CONFIRM_WAIT_(\\d+)', TwoFaConfirmWaitError),
    ('EMAIL_UNCONFIRMED_(\\d+)', EmailUnconfirmedError),
    ('FILE_MIGRATE_(\\d+)', FileMigrateError),
    ('FILE_PART_(\\d+)_MISSING', FilePartMissingError),
    ('FLOOD_TEST_PHONE_WAIT_(\\d+)', FloodTestPhoneWaitError),
    ('FLOOD_WAIT_(\\d+)', FloodWaitError),
    ('INTERDC_(\\d+)_CALL_ERROR', InterdcCallErrorError),
    ('INTERDC_(\\d+)_CALL_RICH_ERROR', InterdcCallRichErrorError),
    ('NETWORK_MIGRATE_(\\d+)', NetworkMigrateError),
    ('PASSWORD_TOO_FRESH_(\\d+)', PasswordTooFreshError),
    ('PHONE_MIGRATE_(\\d+)', PhoneMigrateError),
    ('PREVIOUS_CHAT_IMPORT_ACTIVE_WAIT_(\\d+)MIN', PreviousChatImportActiveWaitMinError),
    ('SESSION_TOO_FRESH_(\\d+)', SessionTooFreshError),
    ('SLOWMODE_WAIT_(\\d+)', SlowModeWaitError),
    ('STATS_MIGRATE_(\\d+)', StatsMigrateError),
    ('TAKEOUT_INIT_DELAY_(\\d+)', TakeoutInitDelayError),
    ('USER_MIGRATE_(\\d+)', UserMigrateError),
)
