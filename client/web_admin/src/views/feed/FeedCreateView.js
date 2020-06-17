import React from "react";
import FontAwesome from 'react-fontawesome';
import { Form, FormGroup, Label, Input, Button,
    Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';
import { ApiFeed } from '../../api';
import { MiscUtils, URLUtils } from "../../../../web_common/extras";
import { DropdownSelection } from "../../components";
import { BlockingComponent } from '../../../../web_common/components';
import { FEED } from "../../config";

export default class FeedCreateView extends React.Component{

    state = {
        feedId: null, // save FeedID when editing
        isProcessing: false, // used for showing loading indicator
        sources: [],
        source: '',
        title: '',
        description: '',
        url: '',
        isShowConfirm: false // confirm popup when deleting
    }


    getSources = (getSourcesCallback) => {
        const callbackSuccess = (response) => {
            const { sources } = response;
            setTimeout(() => {
                this.setState({
                    isProcessing: false,
                    sources: [{text: "-----", value: ""}, ...sources]
                }, () => getSourcesCallback());
            }, 200); //  wait 0.2s, in order to show loading indicator
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


    deleteFeed = () => {
        const { feedId } = this.state;
        const callbackSuccess = (response) => {
            setTimeout(() => {
                URLUtils.moveToURL(FEED.MANAGE);
            }, 500); //  wait 0.5s, in order to show loading indicator
        };
        const callbackError = (error) => {
            MiscUtils.commonCallbackError(this, error);
        };
        const data = { feedId };
        this.setState({isProcessing: true}, () => {
            ApiFeed.delete(callbackSuccess, callbackError, data);
        });
    }


    createOrUpdateFeed = () => {
        const { feedId, source, title, description, url } = this.state;
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
            const data = { feedId, source, title, description, url };
            this.setState({isProcessing: true}, () => {
                ApiFeed.create(callbackSuccess, callbackError, data);
            });
        } else
            MiscUtils.showErrorMessage("All required fields need to be input");
    }


    loadFeed = (feedId) => {
        const callbackSuccess = (response) => {
            const { source_code, title, description, original_url } = response;
            setTimeout(() => {
                this.setState({
                    feedId,
                    isProcessing: false,
                    source: source_code,
                    title, description,
                    url: original_url
                });
            }, 200); //  wait 0.2s, in order to show loading indicator
        };
        const callbackError = (error) => {
            MiscUtils.commonCallbackError(this, error);
        };
        const data = { feedId };
        this.setState({isProcessing: true}, () => {
            ApiFeed.get(callbackSuccess, callbackError, data);
        });
    }


    toggleConfirmPopup = () => {
        this.setState({isShowConfirm: !this.state.isShowConfirm})
    }

    componentDidMount() {
        const getSourcesCallback = () => {
            let pathname = URLUtils.getCurrentPathname();
            if (pathname.indexOf(FEED.EDIT) >= 0) {
                // last element: /feed/edit/xxx --> return xxx
                let feedId = pathname.split('/').slice(-1)[0]
                // in case pathname ends with "/":  /feed/edit/xx/ --> return ""
                if (!feedId)
                    feedId = pathname.split('/').slice(-2)[0]
                this.loadFeed(feedId);
            }
        }

        this.getSources(getSourcesCallback);
    }


    render() {
        const { feedId, isProcessing, sources, source, title, description,
            url, isShowConfirm } = this.state;
        const isSubmittable =  source && title && description;

        return (
            <div className="feedCreateForm">
                <h4 className="paddingVertical20">
                    {
                        !isProcessing &&
                        feedId ? "Feed -Edit" : "Feed - Create"
                    }
                </h4>
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
                        {
                            !isProcessing &&
                            <div>
                                <Button href={FEED.MANAGE}>
                                    <FontAwesome name="angle-left"/> &nbsp; Cancel
                                </Button> &nbsp;&nbsp;
                                <Button color="success" onClick={this.createOrUpdateFeed} disabled={!isSubmittable}>
                                    <FontAwesome name="save"/> &nbsp;
                                    {
                                        feedId ? "Edit" : "Create"
                                    }
                                </Button>&nbsp;&nbsp;
                                {
                                    feedId &&
                                    <Button color="danger" onClick={this.toggleConfirmPopup}>
                                        <FontAwesome name="remove"/> &nbsp;Delete
                                    </Button>
                                }
                            </div>
                        }
                    </Form>
                </BlockingComponent>

                {/* confirm popup when editing */}
                {
                    feedId &&
                    <Modal isOpen={isShowConfirm} toggle={this.toggleConfirmPopup}>
                        <ModalHeader toggle={this.toggleConfirmPopup}>
                            <FontAwesome name="question-circle"/> &nbsp; Confirmation

                        </ModalHeader>
                        <ModalBody>
                            Are you sure to delete?
                        </ModalBody>
                        <ModalFooter>
                            <Button color="secondary" onClick={this.toggleConfirmPopup}>
                                <FontAwesome name="stop"/> &nbsp; Cancel
                            </Button>&nbsp;
                            <Button color="danger" onClick={this.deleteFeed}>
                                <FontAwesome name="remove"/> &nbsp;Delete
                            </Button>
                        </ModalFooter>
                  </Modal>
                }
            </div>
        );
    }

}