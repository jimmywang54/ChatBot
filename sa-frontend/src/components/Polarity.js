import React, { Component } from "react";
import PropTypes from "prop-types";
class Polarity extends Component {
  propTypes = {
    sentence: PropTypes.string.isRequired,
    polarity: PropTypes.string.isRequired
  };
  render() {
    
    return (
      <div>
        ChatBot: "{this.props.polarity}"
      </div>
    );
  }
}
export default Polarity;
