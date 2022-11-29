require "test_helper"

class RegistrationsControllerTest < ActionDispatch::IntegrationTest
    setup do
        @user = users(:one)
        @event = event(:one)
    end

    test "should create registration" do
        assert_difference("Registration.count") do
            post registrations_url, params: { registration: { user_id: @user.id, event_id: @event.id}}
        end

        assert_equal "You have successfully registered for #{@event.title}", flash[:notice]
        assert_redirected_to event_url(@event)
    end

    test "should not create registration with nil user" do
        assert_no_difference("Registration.count") do
            post_registrations_url, params: { registration: { user_id: nil, event_id: @event.id}}
        end

        assert_equal "Invalid email or event", flash[:alert]
        assert_redirected_to events_url
    end

    test "should not create registration with nil event" do
        assert_no_difference("Registration.count") do
            post_registrations_url, params: { registration: { user_id: @user.id, event_id: nil}}
        end

        assert_equal "Invalid email or event", flash[:alert]
        assert_redirected_to events_url
    end
end