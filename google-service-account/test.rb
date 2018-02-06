require 'google/apis/androidpublisher_v2'
require 'googleauth'
require 'pp'

def authorize
  options = JSON.parse(File.read('client_secret.json'))
  key = OpenSSL::PKey::RSA.new(options['private_key'])

  auth = Signet::OAuth2::Client.new(
    token_credential_uri: options['token_uri'],
    audience: options['token_uri'],
    scope: %w(
      https://www.googleapis.com/auth/androidpublisher
    ),
    issuer: options['client_email'],
    signing_key: key
  )
  auth
end

service = Google::Apis::AndroidpublisherV2::AndroidPublisherService.new
service.client_options.application_name = 'Google Play Developer Console Sample'
service.authorization = authorize

response = service.list_reviews('otoshimono.com.lost.mamorio')

pp response
