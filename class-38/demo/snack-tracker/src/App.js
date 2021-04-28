import React, { Component } from 'react';

import './App.css';

class App extends Component {

    constructor(props) {
        super(props);
        this.state = {
            snacks: [
                { id: 1, name: "Coppa", description: "Spicy, please" },
                { id: 2, name: "Licorice", description: "Black, of course" },
            ]
        }
        this.onCreated = this.onCreated.bind(this);
    }

    onCreated(snack) {

        const snacks = [...this.state.snacks, snack];

        snack.id = snacks.length; // One way to generate a unique id for time being

        this.setState({ snacks })


    }

    render() {
        return (
            <div className="App">
                <Header snackCount={this.state.snacks.length} />
                <SnackList snacks={this.state.snacks} onCreated={this.onCreated} />
                <Footer />
            </div>
        );
    }
}

function Header(props) {
    return <h2>Snack Tracker: {props.snackCount}</h2>
}

class SnackList extends Component {

    render() {
        return (
            <div>

            <SnackForm onCreated={this.props.onCreated} />

            <ul>
                {this.props.snacks.map(snack => (
                    <SnackItem key={snack.id} name={snack.name} description={snack.description} />
                    ))}
            </ul>
            </div>
        )
    }
}

class SnackForm extends React.Component {
    constructor(props) {
      super(props);
      this.state = {name: '',description:''};

      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);

      // NOTE: not handling description right now, which is ok for moment but may change
      // If you're curious about flexible way to handle multiple inputs see
      // https://reactjs.org/docs/forms.html#handling-multiple-inputs
    }

    handleChange(event) {
      this.setState({name: event.target.value});
    }

    handleSubmit(event) {
      event.preventDefault();
      this.props.onCreated(this.state);

    }

    render() {
      return (
        <form onSubmit={this.handleSubmit}>
          <label>
            Name:
            <input type="text" value={this.state.name} onChange={this.handleChange} />
          </label>
          <input type="submit" value="Submit" />
        </form>
      );
    }
  }

function SnackItem(props) {
    return <li>{props.name}</li>
}

function Footer() {
    return <h2>Footer soon</h2>
}

export default App;
