'use strict';
import 'bootstrap/dist/css/bootstrap.min.css';

const e = React.createElement;

class JournalApp extends React.Component {
  constructor(props) {
    super(props);
    // TODO init state here?
  }

  render() {
    return (
      <h1>
        Nice
      </h1>
    );
  }
}

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Like'
    );
  }
}

const domContainer = document.querySelector('#journal_app');
ReactDOM.render(e(JournalApp), domContainer)