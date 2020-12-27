import React, { Component } from 'react'
import { FaFacebookMessenger, FaPaypal } from 'react-icons/fa'
export class ContactView extends Component {
    state = {
        name: '',
        email: '',
        subject: '',
        message: '',
    }
    data = {}
    buttonSubmit() {
        alert('Hello')
    }

    render() {
        return (
            <div id="Contact" className="ContactForm">
                <h1>Contact Me</h1>
                <p>For any extra information. Send me message </p>
                <div>

                </div>
                <div className="InputFields">
                    <input
                        type="text"
                        value={this.state.name}
                        onChange={e => this.setState({ name: e.target.value })}
                        placeholder="Name"
                    />
                    <input
                        type="email"
                        value={this.state.email}
                        onChange={e => this.setState({ email: e.target.value })}
                        placeholder="Email"
                    />
                    <input
                        type="text"
                        value={this.state.subject}
                        onChange={e => this.setState({ subject: e.target.value })}
                        placeholder="Subject"
                    />
                    <textarea
                        type="text"
                        value={this.state.message}
                        onChange={e => this.setState({ message: e.target.value })}
                        placeholder="Message"
                    />
                    <button class="btn" onClick={this.buttonSubmit}>
                        <FaFacebookMessenger size="1em" color="white" />  Send Message
                    </button>
                    <button class="btn" onClick={this.buttonSubmit}>
                        <FaPaypal size="1em" color="white" />  Pay Now
                    </button>
                </div>
            </div>
        )
    }
}
export default ContactView
