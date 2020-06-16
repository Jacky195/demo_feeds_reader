import React from 'react';
import { Table, Row, Col, Button } from 'reactstrap';
import Pager from './Pager';
import { DropdownSelection } from "./index";
import { PAGE_SIZE_OPTIONS } from '../config';


export default class DataTable extends React.Component{


    render() {
        return (
            <>
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

                    <Row>
                        <Col sm="1" xs="6">
                            <DropdownSelection optionList={PAGE_SIZE_OPTIONS} />
                        </Col>
                        <Col sm={{ size: 4, offset: 7 }} xs="6" className="paddingTop10">
                            <Pager {...this.props} />
                        </Col>
                    </Row>



            </>
        );
    }

}