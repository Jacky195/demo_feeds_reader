import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, Switch, Redirect } from "react-router-dom";
import { createBrowserHistory } from "history";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'react-notifications/lib/notifications.css';

import './static/App.css';

import App from './App';

const hist = createBrowserHistory();

ReactDOM.render(
    <Router history={hist}>
        <Switch>
            <Route path="/" render={props => <App {...props} />} />
        </Switch>
    </Router>,
    document.getElementById("app")
);