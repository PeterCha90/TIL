import { useParams } from 'react-router-dom'

const data = {
  petercha: {
    name: 'PETER',
    description: 'A normal Developer',
  },
  gildong: {
    name: 'Killdong',
    description:
      'The protagonist of The Legend of Hong Gil-dong, the classic novel',
  },
}

const Profile = () => {
  const params = useParams()
  const profile = data[params.username]

  return (
    <div>
      <h1>사용자 프로필</h1>
      {profile ? (
        <div>
          <h2>{profile.name}</h2>
          <p>{profile.description}</p>
        </div>
      ) : (
        <p>존재하지 않는 프로필입니다</p>
      )}
    </div>
  )
}

export default Profile
