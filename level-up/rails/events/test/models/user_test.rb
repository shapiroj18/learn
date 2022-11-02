require "test_helper"

class UserTest < ActiveSupport::TestCase

  def setup
    @user = User.new(name: "Example User", email: "user@example.com")
  end

  test "email validation should reject invalid addresses" do
    invalid_addresses = %w[user@example,com user_t_foo.org user.name@example.foo@bar_baz.com foo@bar+baz.com]
    invalid_addresses.each do |invalid_address|
      puts invalid_address, @user.valid?
      assert_not @user.valid?, "#{invalid_address.inspect} should be invalid"
    end
  end

  test "email validation shoudl accept valid addresses" do
    valid_addresses = %w[user@example.com user@example.com.br user.last@foo.au]
    valid_addresses.each do |valid_address|
      assert @user.valid?, "#{valid_address.inspect} should be valid"
    end
  end
end
