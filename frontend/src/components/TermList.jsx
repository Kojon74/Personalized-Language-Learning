import React, { Component } from 'react'
import { Card } from 'react-bootstrap'
import Table from 'react-bootstrap/Table'

import './TermList.css'

export default class TermList extends Component {
  constructor(props) {
    super(props);
    this.state= {
      termList: [{
        fromLang: "Hello",
        toLang: "Bonjour",
      },
      {
        fromLang: "Bye",
        toLang: "Aurevoir",
      }],
      fromLang: "English",
      toLang: "French"
    };
  }

  render() {
    const termtable = this.state.termList.map(term => (
      <tr>
        <td>{term.fromLang}</td>
        <td>{term.toLang}</td>
      </tr>
    ));

    return (
      <div className="termlist">
        <div className="card-container">
          <Card className="card" style={{ width: '18rem' }}>
            <Card.Title className="title">Text</Card.Title>
          </Card>
          <Card className="card" style={{ width: '18rem' }}>
            <Card.Title className="title">Flashcards</Card.Title>
          </Card>
          <Card className="card" style={{ width: '18rem' }}>
            <Card.Title className="title">Questions</Card.Title>
          </Card>
        </div>
        <Table className="table" striped>
          <thead className="table-title">
            <tr>
              <th>{this.state.fromLang}</th>
              <th>{this.state.toLang}</th>
            </tr>
          </thead>
          <tbody className="table-list">
            {termtable}
          </tbody>
        </Table>
      </div>
    )
  }
}
