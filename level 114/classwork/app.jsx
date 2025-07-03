import { useState } from "react";

const App = () => {
  // მდგომარეობა მომხმარებლის სახელისა და გვარის შესანახად
  const [userInfo, setUserInfo] = useState({});

  // ფუნქცია, რომელიც იძახება input-ის შეცვლისას
  const handleChange = ({ target }) => {
    const { name, value } = target; // ვიღებთ name-ს და value-ს input-იდან

    // განვაახლებთ userInfo-ს წინა მნიშვნელობების გათვალისწინებით
    setUserInfo(prev => {
      const newUserInfo = { ...prev, [name]: value }; // name გამოიყენება როგორც key
      console.log(newUserInfo); // ვამოწმებთ კონსოლში რას შეიცავს
      return newUserInfo;
    });
  };

  return (
    <>
      {/* სახელი input */}
      <label htmlFor="1">Firstname: </label>
      <input
        type="text"
        name="firstName" // გამოიყენება key-დ userInfo-ში
        id="1"
        onChange={handleChange}
      />

      {/* გვარი input */}
      <input
        type="text"
        name="lastName"
        id="2"
        onChange={handleChange}
      />

      {/* გამოსახვა შემოტანილი მონაცემების */}
      <div>
        <h3>User Info</h3>
        <p>Firstname: {userInfo.firstName || ""}</p>
        <p>Lastname: {userInfo.lastName || ""}</p>
      </div>
    </>
  );
};

export default App;
