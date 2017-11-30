import React, { Component } from 'react';
import ReactDOM from 'react-dom';

export default class FetchGithubGistComp extends Component {
    constructor() {
        super()

        // initialize state
        this.state = {gist: []}
    }

    getGitHubContent() {
        fetch(
            // default GET
            'https://api.github.com/gists'
        ).then(
            // Promise unpacked and resolved as JSON
            res => res.json()
        ).then(
            // JSON content received
            jsonres => {
                // console.log(jsonres)
                this.setState({
                    gist: jsonres
                })
                return null
            }
        )
    }

    componentDidMount() {
        this.getGitHubContent()
    }

    render() {
        var gistContent = this.state.gist;

        if (gistContent.length) {
            return (
                <pre>
                    {JSON.stringify(gistContent, null, "  ")}
                </pre>
            )
        } else {
            return <h2>Loading Gists from GitHub...</h2>
        }

    }
}
