import React from "react";
import { Form, FormGroup, Label, Input, Button } from 'reactstrap';
import { ApiFeed } from '../../api';
import { MiscUtils, URLUtils } from "../../../../web_common/extras";
import { DropdownSelection } from "../../components";
import { BlockingComponent } from '../../../../web_common/components';
import { FEED } from "../../config";

export default class FeedCreateView extends React.Component{

    state = {
        isProcessing: false,
        sources: [],
        source: "",
        title: '',
        description: '',
        url: ''
    }


    getSources = () => {
        const callbackSuccess = (response) => {
            const { sources } = response;
            setTimeout(() => {
                this.setState({
                    isProcessing: false,
                    sources: [{text: "-----", value: ""}, ...sources]
                });
            }, 300); //  wait 0.3s, in order to show loading indicator
        };
        const callbackError = (error) => {
            MiscUtils.commonCallbackError(this, error);
        };
        this.setState({isProcessing: true}, () => {
            ApiFeed.getAllSources(callbackSuccess, callbackError);
        });
    }


    changeSource = (source) => {
        this.setState({source});
    }


    createFeed = () => {
        const { source, title, description, url } = this.state;
        if (source && title && description) {

            const callbackSuccess = (response) => {
                MiscUtils.showNotification('Save success');
                setTimeout(() => {
                    URLUtils.moveToURL(FEED.MANAGE);
                }, 500); //  wait 0.5s, in order to show loading indicator
            };
            const callbackError = (error) => {
                MiscUtils.commonCallbackError(this, error);
            };
            const data = { source, title, description, url };
            this.setState({isProcessing: true}, () => {
                ApiFeed.create(callbackSuccess, callbackError, data);
            });

        } else
            MiscUtils.showErrorMessage("All required fields need to be input");
    }


    componentDidMount() {
        this.getSources();
    }


    render() {
        const { isProcessing, sources, source, title, description, url } = this.state;
        const isSubmittable =  source && title && description;
        return (
            <div className="feedCreateForm">
                <h4 className="paddingVertical20">Feed - Create</h4>
                <BlockingComponent isProcessing={isProcessing}>

                    <Form>
                        <FormGroup>
                            <Label for="exampleSelect">Source</Label>

                            <DropdownSelection optionList={sources}
                                                   onChangeCallback={this.changeSource}
                                                   currentValue={source}
                                />

                        </FormGroup>

                        <FormGroup>
                            <Label for="title">Title (*)</Label>
                            <Input id="title" placeholder="Feed title" value={title}
                                   onChange={(e) => MiscUtils.componentChangeInput(this, e, 'title')} />
                        </FormGroup>

                        <FormGroup>
                            <Label for="description">Description (*)</Label>
                            <Input type="textarea" id="description"  placeholder="Feed description" value={description}
                                   onChange={(e) => MiscUtils.componentChangeInput(this, e, 'description')}/>
                        </FormGroup>

                        <FormGroup>
                            <Label for="url">URL</Label>
                            <Input id="url" placeholder="URL of original feed" value={url}
                                   onChange={(e) => MiscUtils.componentChangeInput(this, e, 'url')} />
                        </FormGroup>


                        <Button href={FEED.MANAGE}>Cancel</Button> &nbsp;&nbsp;
                        <Button color="success" onClick={this.createFeed} disabled={!isSubmittable}>Create</Button>

                    </Form>
                </BlockingComponent>

            </div>
        );
    }

}