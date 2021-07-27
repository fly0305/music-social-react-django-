import React, { Fragment, useEffect, useState } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import {
  getAccessToken,
  getCurrentProfile,
  deleteAccount,
} from '../../actions/profile';
import { Link } from 'react-router-dom';
import DashboardActions from './ DashboardActions';
import Album from './Album';
import Artist from './Artist';
import Track from './Track';
import ArtistRec from '../recommendations/ArtistRec';
import GenreRec from '../recommendations/GenreRec';
import TrackRec from '../recommendations/TrackRec';
import SearchAlbum from '../search/SearchAlbum';
import CustomModal from '../layout/CustomModal';

const Dashboard = ({
  accessToken,
  getCurrentProfile,
  getAccessToken,
  deleteAccount,
  auth: { user, token },
  profile: { profile, loading },
}) => {
  useEffect(() => {
    getAccessToken();
    getCurrentProfile();
  }, []);

  // Get another Spotify Key after every one hour expiration time
  useEffect(() => {
    const interval = setInterval(() => {
      getAccessToken();
    }, 1000 * 60 * 60); // one hour

    return () => clearInterval(interval); // unmount & cleanup
  }, [accessToken]);

  const [showAlbumModal, setShowAlbumModal] = useState(false);

  return (
    <Fragment>
      <h1 className='text-red-500 text-2xl'> Dashboard</h1>
      <p className='lead'>
        <i className='fas fa-user'></i> Welcome{' '}
        {user && user.username.charAt(0).toUpperCase() + user.username.slice(1)}
      </p>
      {profile !== null ? (
        <Fragment>
          {/* Testing Modal purposes */}
          {/* <button
            className='bg-pink-500 text-white active:bg-pink-600 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150'
            type='button'
            onClick={() => setShowModal(true)}
          >
            Open regular modal
          </button> */}

          {showAlbumModal ? (
            <CustomModal
              title='Add your favorite albums'
              component={SearchAlbum}
              setShowModal={setShowAlbumModal}
            />
          ) : null}

          {/*  Testing Modal Purposes */}

          <DashboardActions setShowAlbumModal={setShowAlbumModal} />
          <ArtistRec />
          <GenreRec />
          <TrackRec />
          <div className='flex flex-row gap-x-10'>
            <Album albums={profile.albums} />
            <Artist artists={profile.artists} />
            <Track tracks={profile.tracks} />
          </div>
          <div className='my-2'>
            <button className='btn btn-danger' onClick={() => deleteAccount()}>
              <i className='fas fa-user-minus' /> Delete My Account
            </button>
          </div>
        </Fragment>
      ) : (
        <Fragment>
          <p>You have not yet setup a profile, please add some info</p>
          <Link to='/create-profile' className='btn btn-primary my-1'>
            Create Profile
          </Link>
        </Fragment>
      )}
    </Fragment>
  );
};

Dashboard.propTypes = {
  getCurrentProfile: PropTypes.func.isRequired,
  deleteAccount: PropTypes.func.isRequired,
  auth: PropTypes.object.isRequired,
  profile: PropTypes.object.isRequired,
};

const mapStateToProps = (state) => ({
  auth: state.auth,
  profile: state.profile,
  accessToken: state.profile.accessToken,
});

export default connect(mapStateToProps, {
  getAccessToken,
  getCurrentProfile,
  deleteAccount,
})(Dashboard);
