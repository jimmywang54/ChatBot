import React, { Component } from "react";
import PropTypes from "prop-types";
class Message extends Component {
  propTypes = {
    question: PropTypes.string.isRequired,
    answer: PropTypes.string.isRequired
  };
  render() {
    
    return (
      <div>
        ChatBot: "{this.props.answer}"
      </div>
    );
  }
}
export default Message;
