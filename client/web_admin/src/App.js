import React from 'react';
import { Route, Switch, Redirect } from 'react-router-dom';
import { Container } from 'reactstrap';
import { FeedManageView, FeedCreateView } from './views';
import { FEED }  from './config/routes';


function App() {
    return (
        <Container>
            <Switch>
                <Route exact path={[FEED.CREATE, FEED.EDIT]} component={ FeedCreateView }/>
                <Route path="*" component={ FeedManageView }/>
            </Switch>
        </Container>
    )
}
export default App;