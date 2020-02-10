import React, { Component } from "react";
import "./App.css";
import MuiThemeProvider from "material-ui/styles/MuiThemeProvider";
import TextField from "material-ui/TextField";
import RaisedButton from "material-ui/RaisedButton";
import Paper from "material-ui/Paper";
import Message from "./components/Message";

const style = { marginLeft: 12 };

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      question: "",
      answer: ""
    };
  }

  analyze() {
    fetch("https://localhost:5001/chatbot/message", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ 
        question: this.textField.getValue(),
        answer: ""
       })
    })
      .then(response => response.json())
      .then(data => this.setState(data));
  }

  onEnterPress = e => {
    if (e.key === "Enter") {
      this.analyze();
    }
  };
  render() {
    const messageComponent =
      this.state.answer !== "" ? (
        <Message
          question={this.state.question}
          answer={this.state.answer}
        />
      ) : null;
    return (
      <MuiThemeProvider>
        <div className="centerize">
          <Paper zDepth={1} className="content">
            <h2>Chat Here</h2>
            <TextField
              ref={ref => (this.textField = ref)}
              onKeyUp={this.onEnterPress.bind(this)}
              hintText="Type your question."
            />
            <RaisedButton
              label="Send"
              style={style}
              onClick={this.analyze.bind(this)}
            />{" "}
            {messageComponent}
          </Paper>{" "}
        </div>
      </MuiThemeProvider>
    );
  }
}
export default App;
