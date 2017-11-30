import React, { Component } from "react"
import ReactDOM from "react-dom"

import { BrowserRouter, Route, Link } from "react-router-dom";

import FetchGithubGistComp from "./comp-github-gist/fetchGist";

var someRenderFunc = () => <h2>Info</h2>;

class HelloWorldComponent extends Component {
    render() {
        return (
            <BrowserRouter>
                <div>
                    <h1>Click Link Below</h1>
                    <ul>
                        <li><Link to="/home">Link to Home</Link></li>
                        <li><Link to="/info">Link to Info</Link></li>
                        <li><Link to="/gist">Fetch Gists</Link></li>
                    </ul>
                    <Route path="/home" render={() => <h2>Home</h2>} />
                    <Route path="/info" render={someRenderFunc} />
                    <Route path="/gist" component={FetchGithubGistComp}/>
                </div>
            </BrowserRouter>
        )
    }
}

ReactDOM.render(
    <HelloWorldComponent />,
    document.getElementById('entry-main')
)
