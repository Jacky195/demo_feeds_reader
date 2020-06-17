import React from 'react';
import { Route, Switch } from 'react-router-dom';
import {NotificationContainer} from 'react-notifications';
import { Container } from 'reactstrap';
import { FeedManageView, FeedCreateView } from './views';
import { FEED }  from './config';


function App() {
    return (
        <Container>
            <Switch>
                <Route path={[FEED.CREATE, FEED.EDIT]} component={ FeedCreateView }/>
                <Route path="*" component={ FeedManageView }/>
            </Switch>

            <NotificationContainer/>

        </Container>
    )
}
export default App;