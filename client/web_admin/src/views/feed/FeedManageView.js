import React from "react";
import { Table, Row, Col, InputGroup, InputGroupAddon, Button, Input, FormGroup, Label} from 'reactstrap';
import { Pager } from '../../components';


export default class FeedManageView extends React.Component{


    render() {
        return (
            <div>
                <h4 className="paddingVertical20">Feed Management</h4>
                <Row>

                    <Col sm="3" xs="6">
                        <InputGroup>
                            <Input placeholder="Filter by Source" />
                            <InputGroupAddon addonType="append">
                                <Button color="success">Search</Button>
                            </InputGroupAddon>
                        </InputGroup>
                    </Col>


                    <Col sm={{ size: 2, offset: 5 }} xs="6">
                        <FormGroup>
                            <Input type="select" name="select">
                              <option>5 per page</option>
                              <option>10 per page</option>
                            </Input>
                          </FormGroup>
                    </Col>


                    <Col sm="2" xs="12">
                        <Button outline color="danger" size="md">+ Add</Button>
                    </Col>

                </Row>



                <Table hover responsive size="sm">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>Source</th>
                      <th>Title</th>
                      <th>Description</th>
                        <th>Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <th scope="row">1</th>
                      <td>washingtonpost</td>
                      <td>djsf kdsjfb kdb dskf</td>
                      <td>jkadf dsfh dskfgb dflbfskd</td>
                        <td>
                            <Button outline color="primary" size="sm">Edit</Button>
                        </td>
                    </tr>
                    <tr>
                      <th scope="row">2</th>
                      <td>washingtonpost</td>
                      <td>f dslfkj sdlgfsdg gd</td>
                      <td>@fat</td>
                        <td><Button outline color="primary" size="sm">Edit</Button></td>
                    </tr>
                    <tr>
                      <th scope="row">3</th>
                      <td>feedforall</td>
                      <td>the Bird</td>
                      <td>f dslkfj rlodflgfd</td>
                        <td><Button outline color="primary" size="sm">Edit</Button></td>
                    </tr>
                  </tbody>
                </Table>


                <Pager/>
            </div>
        );
    }

}