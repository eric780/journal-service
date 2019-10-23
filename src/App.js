import React from 'react';
import logo from './logo.svg';
import './App.css';

import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import axios from 'axios';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <JournalEntrySearchComponent/>
    </div>
  );
}

class JournalEntrySearchComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      searchText: "",
    };

    this.handleSubmit = this.handleSubmit.bind(this);
    this.onSearchTextChanged = this.onSearchTextChanged.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();
    const form = event.currentTarget;
    console.log(event);
    console.log("clicked");
    console.log("value: ", this.state.searchText);
    axios.get("http://localhost:8000/api/entries").then(res => console.log(res));
  }

  onSearchTextChanged(event) {
    this.setState({searchText: event.target.value});
  }

  render() {
    return (
      <Form onSubmit={this.handleSubmit}>
        <Form.Group>
          <Form.Label>Date</Form.Label>
          <Form.Control placeholder="YYYY-MM-DD" onChange={this.onSearchTextChanged}/>
        </Form.Group>
        <Button variant="primary" size="lg" type="submit">
          Search For Entry
        </Button>
      </Form>
    );
  }
}

export default App;
