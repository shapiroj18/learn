class User < ApplicationRecord
    VALID_EMAIL_REGEX = /\A\S+@.+\.\S+\z/.freeze
    validates :email, format: { with: VALID_EMAIL_REGEX }

    has_many :registrations, dependent: :destroy
    has_many :events, through: registrations
end
