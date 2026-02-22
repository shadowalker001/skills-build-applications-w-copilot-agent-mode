
import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  // -8000.app.github.dev/api/teams
  useEffect(() => {
    fetch(endpoint)
      .then(res => {
        if (!res.ok) throw new Error('Network response was not ok');
        return res.json();
      })
      .then(data => {
        console.log('Teams endpoint:', endpoint);
        console.log('Fetched teams:', data);
        setTeams(data.results ? data.results : data);
      })
      .catch(err => {
        console.error('Error fetching teams:', err);
        setTeams([]);
      });
  }, [endpoint]);

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4 text-primary">Teams</h2>
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead className="table-dark">
              <tr>
                <th>#</th>
                <th>Name</th>
                <th>Members</th>
              </tr>
            </thead>
            <tbody>
              {teams.length === 0 ? (
                <tr><td colSpan="3">No data available</td></tr>
              ) : (
                teams.map((team, idx) => (
                  <tr key={idx}>
                    <td>{idx + 1}</td>
                    <td>{team.name || team.id || JSON.stringify(team)}</td>
                    <td>{team.members ? team.members.length : '-'}</td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Teams;
